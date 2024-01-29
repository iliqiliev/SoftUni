def rectangle(length: int, width: int) -> str:
    def area() -> int:
        return length * width

    def perimeter() -> int:
        return 2 * (length + width)

    if not all(isinstance(side, int) for side in (length, width)):
        return "Enter valid values!"

    return (f"Rectangle area: {area()}\n"
            f"Rectangle perimeter: {perimeter()}")
