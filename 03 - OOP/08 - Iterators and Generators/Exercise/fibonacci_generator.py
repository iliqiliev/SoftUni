from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    current, following = 0, 1

    while True:
        yield current

        current, following = following, following + current
