from functools import reduce
import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def operate(operation: str, *numbers: int) -> float:
    return reduce(operators[operation], numbers)
