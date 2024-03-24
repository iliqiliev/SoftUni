from functools import wraps
from typing import Callable, Dict


def cache(fibonacci: Callable[[int], int]) -> Callable[[int], int]:
    log: Dict[int, int] = {}
    fibonacci.log = log  # can't type function attributes directly

    @wraps(fibonacci)
    def wrapper(term: int) -> int:
        if term not in fibonacci.log:
            fibonacci.log[term] = fibonacci(term)

        return fibonacci.log[term]

    return wrapper
