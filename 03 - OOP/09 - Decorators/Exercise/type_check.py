from functools import wraps
from itertools import chain
from typing import Any, Callable, Type


def type_check(
    parameter_type: Type[Any]
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if not all(
                isinstance(argument, parameter_type)
                for argument in chain(args, kwargs.items())
            ):
                return "Bad Type"

            return func(*args, **kwargs)

        return wrapper

    return decorator
