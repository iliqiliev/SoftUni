from typing import Callable


def func_executor(*functions_and_arguments: Callable and tuple) -> str:
    result = []

    for function, arguments in functions_and_arguments:
        result.append(f"{function.__name__} - {function(*arguments)}")

    return "\n".join(result)
