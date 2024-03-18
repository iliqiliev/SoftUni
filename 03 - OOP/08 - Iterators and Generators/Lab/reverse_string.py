from typing import Generator


def reverse_text(text: str) -> Generator[str, None, None]:
    for char in reversed(text):
        yield char
