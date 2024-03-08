from collections import defaultdict
from typing import DefaultDict
from project import Dough, Topping


class Pizza:
    def __init__(
            self, name: str, dough: Dough, max_number_of_toppings: int
    ) -> None:

        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: DefaultDict[str, float] = defaultdict(float)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("The name cannot be an empty string")

        self.__name = name

    @property
    def dough(self) -> Dough:
        return self.__dough

    @dough.setter
    def dough(self, dough: Dough) -> None:
        if dough is None:
            raise ValueError("You should add dough to the pizza")

        self.__dough = dough

    @property
    def max_number_of_toppings(self) -> int:
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, max_number_of_toppings: int) -> None:
        if max_number_of_toppings <= 0:
            raise ValueError(
                "The maximum number of toppings cannot be less or equal to zero"
            )

        self.__max_number_of_toppings = max_number_of_toppings

    def add_topping(self, topping: Topping) -> None:
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> float:
        return self.dough.weight + sum(self.toppings.values())
