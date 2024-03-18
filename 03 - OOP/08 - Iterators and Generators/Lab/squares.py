from typing import Generator


def squares(target: int) -> Generator[int, None, None]:
    for number in range(1, target + 1):
        yield number ** 2
