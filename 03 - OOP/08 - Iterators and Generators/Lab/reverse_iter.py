from typing import Any, Sequence


class reverse_iter:
    def __init__(self, sequence: Sequence[Any]) -> None:
        self.sequence = sequence
        self.index = len(sequence) - 1

    def __iter__(self) -> "reverse_iter":
        return self

    def __next__(self) -> Any:
        if self.index < 0:
            raise StopIteration

        self.index -= 1
        return self.sequence[self.index + 1]
