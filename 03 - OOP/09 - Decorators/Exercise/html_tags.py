from functools import wraps
from typing import Any, Callable


StrReturnType = Callable[..., str]


def tags(tag: str) -> Callable[[StrReturnType], StrReturnType]:
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"

    def decorator(func: StrReturnType) -> StrReturnType:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            return f"{start_tag}{func(*args, **kwargs)}{end_tag}"

        return wrapper

    return decorator
