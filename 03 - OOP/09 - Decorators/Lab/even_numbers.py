from functools import wraps
from typing import Callable, List


def even_numbers(func: Callable[..., List[int]]) -> Callable[..., List[int]]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> List[int]:
        return [num for num in func(*args, **kwargs) if not num % 2]

    return wrapper
