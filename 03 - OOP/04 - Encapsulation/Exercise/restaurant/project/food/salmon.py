from project.food import MainDish


class Salmon(MainDish):
    GRAMS: float = 22

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, self.GRAMS)
