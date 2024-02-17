from functools import reduce
from operator import mul


def multiply(*numbers: int) -> int:
    return reduce(mul, numbers)
