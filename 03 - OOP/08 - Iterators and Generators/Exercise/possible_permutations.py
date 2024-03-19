from itertools import permutations
from typing import Any, Generator, List


def possible_permutations(
        numbers: List[Any]
) -> Generator[List[Any], None, None]:

    yield from map(list, permutations(numbers))
