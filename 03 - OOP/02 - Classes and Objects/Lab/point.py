class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def set_x(self, new_x: float) -> None:
        self.x = new_x

    def set_y(self, new_y: float) -> None:
        self.y = new_y

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"
