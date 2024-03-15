from project.animals import Mammal
from project import Vegetable, Fruit, Meat


class Mouse(Mammal):
    _FOODS_EATEN = {Vegetable, Fruit}
    _FOOD_WEIGHT_GAIN_COEFFICIENT = 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    _FOODS_EATEN = {Meat}
    _FOOD_WEIGHT_GAIN_COEFFICIENT = 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    _FOODS_EATEN = {Vegetable, Meat}
    _FOOD_WEIGHT_GAIN_COEFFICIENT = 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    _FOODS_EATEN = {Meat}
    _FOOD_WEIGHT_GAIN_COEFFICIENT = 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
