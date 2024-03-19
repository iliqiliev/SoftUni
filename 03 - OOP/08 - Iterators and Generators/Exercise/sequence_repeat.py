from typing import Any, Sequence


class sequence_repeat:
    def __init__(self, sequence: Sequence[Any], repeats: int) -> None:
        self.sequence = sequence
        self.repeats = repeats

        self.index = -1
        self.length = len(sequence)

    def __iter__(self) -> "sequence_repeat":
        return self

    def __next__(self) -> Any:
        self.index += 1

        if self.index >= self.repeats:
            raise StopIteration

        return self.sequence[self.index % self.length]
