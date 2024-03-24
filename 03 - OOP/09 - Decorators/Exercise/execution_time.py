from functools import wraps
from time import time
from typing import Any, Callable


def exec_time(func: Callable[..., Any]) -> Callable[..., float]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> float:
        start = time()
        func(*args, **kwargs)
        end = time()

        return end - start

    return wrapper
