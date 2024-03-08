from project.food import Dessert


class Cake(Dessert):
    GRAMS: float = 250
    CALORIES: float = 1000
    PRICE: float = 5

    def __init__(self, name: str) -> None:
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)
