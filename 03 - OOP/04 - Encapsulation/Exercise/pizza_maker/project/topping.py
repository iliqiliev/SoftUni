class Topping:
    def __init__(self, topping_type: str, weight: float) -> None:
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self) -> str:
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, topping_type: str) -> None:
        if not topping_type:
            raise ValueError("The topping type cannot be an empty string")

        self.__topping_type = topping_type

    @property
    def weight(self) -> float:
        return self.__weight + 1

    @weight.setter
    def weight(self, weight: float) -> None:
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

        self.__weight = weight
