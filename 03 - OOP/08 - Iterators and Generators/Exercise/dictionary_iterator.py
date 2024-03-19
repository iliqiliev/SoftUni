from typing import Any, Dict, Tuple


class dictionary_iter:
    def __init__(self, dictionary: Dict[Any, Any]) -> None:
        self.data = tuple(dictionary.items())
        self.length = len(dictionary)
        self.index = 0

    def __iter__(self) -> "dictionary_iter":
        return self

    def __next__(self) -> Tuple[Any, Any]:
        if self.index >= self.length:
            raise StopIteration

        self.index += 1
        return self.data[self.index - 1]
