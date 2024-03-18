from typing import Generator


def genrange(start: int, end: int) -> Generator[int, None, None]:
    for number in range(start, end + 1):
        yield number
