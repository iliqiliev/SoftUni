from typing import List


def number_increment(numbers: List[int]) -> List[int]:
    def increase():
        return [number + 1 for number in numbers]

    return increase()
