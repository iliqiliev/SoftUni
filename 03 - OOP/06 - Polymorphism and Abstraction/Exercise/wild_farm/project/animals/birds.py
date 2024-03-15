from project.animals import Bird
from project import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    _FOODS_EATEN = {Meat}
    _FOOD_WEIGHT_GAIN_COEFFICIENT = 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):
    _FOODS_EATEN = {Vegetable, Fruit, Meat, Seed}
    _FOOD_WEIGHT_GAIN_COEFFICIENT = 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
