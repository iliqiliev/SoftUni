from itertools import islice
from typing import Any, Callable, Generator, Iterable, List, Tuple


def solution() -> Tuple[
    Callable[[int, Iterable[Any]], List[Any]],
    Callable[[], Generator[float, None, None]],
    Callable[[], Generator[int, None, None]],
]:  # SoftUni be like

    def integers() -> Generator[int, None, None]:
        number = 1

        while True:
            yield number
            number += 1

    def halves() -> Generator[float, None, None]:
        for number in integers():
            yield number / 2

    def take(count: int, sequence: Iterable[Any]) -> List[Any]:
        return list(islice(sequence, count))

    return (take, halves, integers)
