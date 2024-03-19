class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        
        self.current = 0

    def __iter__(self) -> "take_skip":
        return self

    def __next__(self) -> int:
        if self.current >= self.count:
            raise StopIteration

        self.current += 1
        return (self.current - 1) * self.step
