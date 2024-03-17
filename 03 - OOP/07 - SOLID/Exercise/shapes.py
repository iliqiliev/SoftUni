from abc import ABC, abstractmethod
from math import sqrt
from typing import Optional


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float: ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height


class Triange(Shape):
    def __init__(self, base: float, height: Optional[float] = None) -> None:
        self.base = base
        self.height = height

    @property
    def area(self) -> float:
        return 0.5 * self.base * self.height

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: Optional[float]) -> None:
        if height is None:
            height = 0.5 * sqrt(3) * self.base

        self.__height = height


class AreaCalculator:
    def __init__(self, *shapes: Shape):
        self.shapes = [*shapes]

    @property
    def shapes(self) -> list[Shape]:
        return self.__shapes

    @shapes.setter
    def shapes(self, shapes: list[Shape]) -> None:
        if not isinstance(shapes, list):
            raise TypeError(f"Shapes must be in {list}")

        if not all(isinstance(shape, Shape) for shape in shapes):
            raise ValueError(f"All elements must be {Shape}")

        self.__shapes = shapes

    @property
    def total_area(self) -> float:
        return sum(shape.area for shape in self.shapes)


def main():
    shapes = [Rectangle(2, 3), Rectangle(1, 6)]
    calculator = AreaCalculator(*shapes)
    print("The total area is: ", calculator.total_area)

    calculator.shapes.append(Triange(2, 2))
    print("The total area is: ", calculator.total_area)

    calculator.shapes.append(Triange(2))  # equilateral triangle
    print("The total area is: ", calculator.total_area)


if __name__ == "__main__":
    main()
