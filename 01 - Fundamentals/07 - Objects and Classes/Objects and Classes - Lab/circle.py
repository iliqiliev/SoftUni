class Circle:
    __pi = 3.14

    def __init__(self, diameter) -> None:
        self.diameter = diameter

    def calculate_circumference(self) -> float:
        # пd
        return (Circle.__pi * self.diameter)

    def calculate_area(self) -> float:
        # пr**2
        return (Circle.__pi * (self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle) -> float:
        # area multiplied by the ration of the angle to a full circle
        return ((Circle.calculate_area(self)) * (angle / 360))
