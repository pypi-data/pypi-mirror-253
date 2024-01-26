""" Hooks sub-package - houses log_this and other hooks. """
import time
from typing import Any, Callable, Optional

from pplog.factory import get_class
from pplog.integrations import http
from pplog.log_checks.check_model import LogCheckResult


def log_this(key: str, output_check: bool = True) -> Callable:
    """Wrapper function

    Args:
        key (str): ppconf identifier key
        output_check (bool - Optional - defaults to True): whether to log the result
            of the LogCheck on func's output
    """

    def decorator(func) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            check_class, check_class_arguments = get_class(key)
            # Call the original function
            result = func(*args, **kwargs)
            if output_check:
                check_class(key, result, check_class_arguments).log()
            return result

        return wrapper

    return decorator


async def async_check_fast_api_http_request(
    key: str, request: http.Request, call_next
) -> http.Response:
    """Async hook for fast api http request middleware."""
    start_time = time.time()
    response = await call_next(request)
    elapsed_time_in_ms = time.time() - start_time * 1000
    check_fast_api_http_request(
        key=key, request=request, response=response, elapsed_time_in_ms=elapsed_time_in_ms
    )
    return response


def check_fast_api_http_request(
    key: str, request: http.Request, response: http.Response, elapsed_time_in_ms: float
) -> Optional[LogCheckResult]:
    """Main logic for fast api request middleware.

    The core logic is implemented in sync function
    to make testing easier and not require additional hacking
    of the asyncio event loop.
    """
    check_class, check_class_arguments = get_class(key)
    if check_class_arguments.get("method", "").lower() != str(request.method).lower():
        return None

    if check_class_arguments.get("url_pattern", "") not in str(request.url):
        return None

    checker = check_class(key, request, response, elapsed_time_in_ms, check_class_arguments)
    log_result: LogCheckResult = checker.check()
    checker.log(log_result)

    return log_result


def log_check_float(key: str, float_value: float):
    """Simple Hook to check a float value against monitoring configuration.

    Useful when a more specific hook is not available for the use case.
    """
    check_class, check_class_arguments = get_class(key)
    check_class(key, float_value, check_class_arguments).log()
