from typing import Any, Generator, Iterable


def read_next(*iterables: Iterable[Any]) -> Generator[Any, None, None]:
    for iterable in iterables:
        yield from iterable
