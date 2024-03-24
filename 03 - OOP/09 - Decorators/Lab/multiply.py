from functools import wraps
from typing import Callable, TypeVar


RepeatableType = TypeVar("RepeatableType", int, float, complex, str)


def multiply(
    multiplier: int
) -> Callable[[Callable[..., RepeatableType]], Callable[..., RepeatableType]]:

    def decorator(
        func: Callable[..., RepeatableType]
    ) -> Callable[..., RepeatableType]:

        @wraps(func)
        def wrapper(*args, **kwargs) -> RepeatableType:
            return func(*args, **kwargs) * multiplier

        return wrapper

    return decorator
