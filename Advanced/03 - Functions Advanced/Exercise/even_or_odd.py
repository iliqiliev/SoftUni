from typing import List


def even_odd(*numbers_and_parity: int and str) -> List[int]:
    numbers = numbers_and_parity[:-1]
    parity = numbers_and_parity[-1]

    if parity == "odd":
        return [num for num in numbers if num & 1]

    return [num for num in numbers if not num & 1]
