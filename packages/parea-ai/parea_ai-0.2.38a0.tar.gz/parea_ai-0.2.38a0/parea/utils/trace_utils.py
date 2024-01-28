from typing import Any, Callable, Optional

import contextvars
import inspect
import json
import logging
import os
import threading
import time
from collections import ChainMap
from functools import wraps

from parea.constants import PAREA_OS_ENV_EXPERIMENT_UUID
from parea.helpers import gen_trace_id, to_date_and_time_string
from parea.parea_logger import parea_logger
from parea.schemas.models import NamedEvaluationScore, TraceLog
from parea.utils.universal_encoder import json_dumps

logger = logging.getLogger()


# Context variable to maintain the current trace context stack
trace_context = contextvars.ContextVar("trace_context", default=[])

# A dictionary to hold trace data for each trace
trace_data = contextvars.ContextVar("trace_data", default={})

# Context variable to maintain running evals in thread
thread_ids_running_evals = contextvars.ContextVar("thread_ids_running_evals", default=[])


def merge(old, new):
    if isinstance(old, dict) and isinstance(new, dict):
        return dict(ChainMap(new, old))
    if isinstance(old, list) and isinstance(new, list):
        return old + new
    return new


def get_current_trace_id() -> str:
    stack = trace_context.get()
    if stack:
        return stack[-1]
    return ""


def trace_insert(data: dict[str, Any]):
    current_trace_id = get_current_trace_id()
    current_trace_data: TraceLog = trace_data.get()[current_trace_id]

    for key, new_value in data.items():
        existing_value = current_trace_data.__getattribute__(key)
        current_trace_data.__setattr__(key, merge(existing_value, new_value) if existing_value else new_value)


def trace(
    name: Optional[str] = None,
    tags: Optional[list[str]] = None,
    metadata: Optional[dict[str, Any]] = None,
    target: Optional[str] = None,
    end_user_identifier: Optional[str] = None,
    eval_funcs_names: Optional[list[str]] = None,
    eval_funcs: Optional[list[Callable]] = None,
    access_output_of_func: Optional[Callable] = None,
):
    def init_trace(func_name, args, kwargs, func) -> tuple[str, float]:
        start_time = time.time()
        trace_id = gen_trace_id()
        trace_context.get().append(trace_id)

        sig = inspect.signature(func)
        parameters = sig.parameters

        inputs = {k: v for k, v in zip(parameters.keys(), args)}
        inputs.update(kwargs)
        # filter out any values which aren't JSON serializable
        for k, v in inputs.items():
            try:
                json.dumps(v)
            except TypeError:
                inputs[k] = str(v)

        trace_data.get()[trace_id] = TraceLog(
            trace_id=trace_id,
            parent_trace_id=trace_id,
            start_timestamp=to_date_and_time_string(start_time),
            trace_name=name or func_name,
            end_user_identifier=end_user_identifier,
            metadata=metadata,
            target=target,
            tags=tags,
            inputs=inputs,
            experiment_uuid=os.environ.get(PAREA_OS_ENV_EXPERIMENT_UUID, None),
        )
        parent_trace_id = trace_context.get()[-2] if len(trace_context.get()) > 1 else None
        if parent_trace_id:
            trace_data.get()[trace_id].parent_trace_id = parent_trace_id
            trace_data.get()[parent_trace_id].children.append(trace_id)

        return trace_id, start_time

    def cleanup_trace(trace_id, start_time):
        end_time = time.time()
        trace_data.get()[trace_id].end_timestamp = to_date_and_time_string(end_time)
        trace_data.get()[trace_id].latency = end_time - start_time
        thread_eval_funcs_then_log(trace_id, eval_funcs, access_output_of_func)
        trace_context.get().pop()

    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            trace_id, start_time = init_trace(func.__name__, args, kwargs, func)
            output_as_list = check_multiple_return_values(func)
            try:
                result = await func(*args, **kwargs)
                trace_data.get()[trace_id].output = make_output(result, output_as_list)
                trace_data.get()[trace_id].status = "success"
                trace_data.get()[trace_id].evaluation_metric_names = eval_funcs_names
            except Exception as e:
                logger.exception(f"Error occurred in function {func.__name__}, {e}")
                trace_data.get()[trace_id].error = str(e)
                trace_data.get()[trace_id].status = "error"
                raise e
            finally:
                cleanup_trace(trace_id, start_time)
            return result

        @wraps(func)
        def wrapper(*args, **kwargs):
            trace_id, start_time = init_trace(func.__name__, args, kwargs, func)
            output_as_list = check_multiple_return_values(func)
            try:
                result = func(*args, **kwargs)
                trace_data.get()[trace_id].output = make_output(result, output_as_list)
                trace_data.get()[trace_id].status = "success"
                trace_data.get()[trace_id].evaluation_metric_names = eval_funcs_names
            except Exception as e:
                logger.exception(f"Error occurred in function {func.__name__}, {e}")
                trace_data.get()[trace_id].error = str(e)
                trace_data.get()[trace_id].status = "error"
                raise e
            finally:
                cleanup_trace(trace_id, start_time)
            return result

        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return wrapper

    if callable(name):
        func = name
        name = None
        return decorator(func)

    return decorator


def check_multiple_return_values(func) -> bool:
    specs = inspect.getfullargspec(func)
    try:
        r = specs.annotations.get("return", None)
        if r and r.__origin__ == tuple:
            return len(r.__args__) > 1
    except Exception:
        return False


def make_output(result, islist) -> str:
    if islist:
        json_list = [json_dumps(r) for r in result]
        return json_dumps(json_list)
    elif isinstance(result, str):
        return result
    else:
        return json_dumps(result)


def logger_record_log(trace_id: str):
    logging_thread = threading.Thread(
        target=parea_logger.record_log,
        kwargs={"data": trace_data.get()[trace_id]},
    )
    logging_thread.start()


def logger_all_possible(trace_id: str):
    logging_thread = threading.Thread(
        target=parea_logger.default_log,
        kwargs={"data": trace_data.get()[trace_id]},
    )
    logging_thread.start()


def call_eval_funcs_then_log(trace_id: str, eval_funcs: list[Callable] = None, access_output_of_func: Callable = None):
    data = trace_data.get()[trace_id]
    thread_ids_running_evals.get().append(trace_id)
    try:
        if eval_funcs and data.status == "success":
            if access_output_of_func:
                output = json.loads(data.output)
                output = access_output_of_func(output)
                output_for_eval_metrics = json_dumps(output)
            else:
                output_for_eval_metrics = data.output

            data.output_for_eval_metrics = output_for_eval_metrics
            output_old = data.output
            data.output = data.output_for_eval_metrics
            data.scores = []

            for func in eval_funcs:
                try:
                    score = func(data)
                    data.scores.append(NamedEvaluationScore(name=func.__name__, score=score))
                except Exception as e:
                    logger.exception(f"Error occurred calling evaluation function '{func.__name__}', {e}", exc_info=e)

            data.output = output_old
    except Exception as e:
        logger.exception(f"Error occurred in when trying to evaluate output, {e}", exc_info=e)
    finally:
        thread_ids_running_evals.get().remove(trace_id)
    parea_logger.default_log(data=data)


def thread_eval_funcs_then_log(trace_id: str, eval_funcs: list[Callable] = None, access_output_of_func: Callable = None):
    logging_thread = threading.Thread(
        target=call_eval_funcs_then_log,
        kwargs={"trace_id": trace_id, "eval_funcs": eval_funcs, "access_output_of_func": access_output_of_func},
    )
    logging_thread.start()
