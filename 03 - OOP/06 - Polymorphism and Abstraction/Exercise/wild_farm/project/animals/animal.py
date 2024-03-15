from abc import ABC, abstractmethod
from typing import Optional, Set, Type
from project import Food


class Animal(ABC):
    _FOODS_EATEN: Set[Type[Food]] = set()
    _FOOD_WEIGHT_GAIN_COEFFICIENT: float = 0.0

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @staticmethod
    @abstractmethod
    def make_sound(): ...

    def feed(self, food: Food) -> Optional[str]:
        if type(food) not in self._FOODS_EATEN:
            return (
                f"{self.__class__.__name__} does not eat "
                f"{food.__class__.__name__}!"
            )

        self.food_eaten += food.quantity
        self.weight += food.quantity * self._FOOD_WEIGHT_GAIN_COEFFICIENT

        return None


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} "
            f"[{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
        )


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} "
            f"[{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
        )
