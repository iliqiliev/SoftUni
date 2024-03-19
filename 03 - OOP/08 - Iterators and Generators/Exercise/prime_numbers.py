from math import sqrt
from typing import Generator, List


def get_primes(numbers: List[int]) -> Generator[int, None, None]:
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                break

        else:
            yield number
