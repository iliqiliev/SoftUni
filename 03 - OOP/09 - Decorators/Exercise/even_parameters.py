from functools import wraps
from itertools import chain
from typing import Callable, TypeVar, Union


T = TypeVar("T")


def even_parameters(func: Callable[..., T]) -> Callable[..., Union[T, str]]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Union[T, str]:
        for argument in chain(args, kwargs.values()):
            if not isinstance(argument, int) or argument % 2:
                return "Please use only even numbers!"

        return func(*args, *kwargs)

    return wrapper
