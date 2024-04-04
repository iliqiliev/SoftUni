from abc import ABC, abstractmethod
from typing import List, Optional


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int) -> None:
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")

        self.__name = name

    @property
    def elevation(self) -> int:
        return self.__elevation

    @elevation.setter
    def elevation(self, elevation: int) -> None:
        if elevation < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")

        self.__elevation = elevation

    @abstractmethod
    def get_recommended_gear(self) -> List[str]: ...

    @abstractmethod
    def calculate_difficulty_level(self) -> Optional[str]: ...
