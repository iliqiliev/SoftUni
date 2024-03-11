import operator
from functools import reduce
from typing import Union


Number = Union[int, float, complex]


class Calculator:

    @staticmethod
    def add(*numbers: Number) -> Number:
        return sum(numbers)

    @staticmethod
    def subtract(*numbers: Number) -> Number:
        return reduce(operator.sub, numbers)

    @staticmethod
    def multiply(*numbers: Number) -> Number:
        return reduce(operator.mul, numbers)

    @staticmethod
    def divide(*numbers: Number) -> Number:
        return reduce(operator.truediv, numbers)
