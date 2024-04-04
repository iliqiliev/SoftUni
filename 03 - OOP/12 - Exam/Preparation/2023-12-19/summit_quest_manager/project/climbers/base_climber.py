from abc import ABC, abstractmethod
from typing import List
from project.peaks import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float) -> None:
        self.name = name
        self.strength = strength
        self.conquered_peaks: List[str] = []
        self.is_prepared: bool = True

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Climber name cannot be null or empty!")

        self.__name = name

    @property
    def strength(self) -> float:
        return self.__strength

    @strength.setter
    def strength(self, strength: float) -> None:
        if strength <= 0:
            raise ValueError(
                "A climber cannot have negative strength or strength equal to 0!"
            )

        self.__strength = strength

    @property
    @abstractmethod
    def min_strength(self) -> float: ...

    def can_climb(self) -> bool:
        return self.strength >= self.min_strength

    @abstractmethod
    def climb(self, peak: BasePeak) -> None: ...

    def rest(self) -> None:
        self.strength += 15

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}: /// "
            f"Climber name: {self.name} * Left strength: {self.strength:.1f} * "
            f"Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///"
        )
