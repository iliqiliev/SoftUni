class Flower:
    def __init__(self, name: str, water_requirements: int) -> None:
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f"{self.name} is {'not ' * (not self.is_happy)}happy"
