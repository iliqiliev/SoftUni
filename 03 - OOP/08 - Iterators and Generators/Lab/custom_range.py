class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __iter__(self) -> "custom_range":
        return self

    def __next__(self) -> int:
        if self.start > self.end:
            raise StopIteration

        self.start += 1
        return self.start - 1
