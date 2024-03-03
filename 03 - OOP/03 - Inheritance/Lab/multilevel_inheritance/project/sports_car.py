from project.car import Car


class SportsCar(Car):  # pylint: disable=too-few-public-methods
    def race(self) -> str:
        return "racing..."
