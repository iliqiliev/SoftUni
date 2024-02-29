class Glass:
    capacity = 250

    def __init__(self) -> None:
        self.content: int = 0

    def space_left(self) -> int:
        return Glass.capacity - self.content

    def fill(self, ml: int) -> str:
        if ml > self.space_left():
            return f"Cannot add {ml} ml"

        self.content += ml

        return f"Glass filled with {ml} ml"

    def empty(self) -> str:
        self.content = 0

        return "Glass is now empty"

    def info(self) -> str:
        return f"{self.space_left()} ml left"
