from project.beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS: float = 50
    PRICE: float = 3.50

    def __init__(self, name: str, caffeine: float) -> None:
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self) -> float:
        return self.__caffeine
