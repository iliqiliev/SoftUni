VOWELS = "aeiouy"


class vowels:
    def __init__(self, string: str) -> None:
        self.string = string
        self.index = 0

    def __iter__(self) -> "vowels":
        return self

    def __next__(self) -> str:
        try:
            while self.string[self.index].lower() not in VOWELS:
                self.index += 1

        except IndexError as error:
            raise StopIteration from error

        self.index += 1
        return self.string[self.index - 1]
