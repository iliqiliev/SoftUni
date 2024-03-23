from functools import wraps
from typing import Callable, List


VOWELS = "aeiouy"


def vowel_filter(func: Callable[..., List[str]]) -> Callable[..., List[str]]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> List[str]:
        return [
            char for char in func(*args, **kwargs) if char.lower() in VOWELS
        ]

    return wrapper
