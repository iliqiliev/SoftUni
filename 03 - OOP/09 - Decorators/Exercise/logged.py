from functools import wraps
from typing import Any, Callable


def logged(func: Callable[..., Any]) -> Callable[..., str]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        arguments = ", ".join(filter(None, (  # filter items that are True
            ", ".join(map(str, args)),
            ", ".join(f"{key}={value}" for key, value in kwargs.items())
        )))

        return (
            f"you called {func.__name__}({arguments})\n"
            f"it returned {func(*args, **kwargs)}"
        )

    return wrapper
