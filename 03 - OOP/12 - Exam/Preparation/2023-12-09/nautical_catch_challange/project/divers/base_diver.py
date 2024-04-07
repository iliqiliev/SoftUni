from abc import ABC, abstractmethod
from typing import List
from project.fish import BaseFish


class BaseDiver(ABC):
    DEFAULT_OXYGEN_LEVEL: float = 0

    def __init__(self, name: str, oxygen_level: float = 0) -> None:
        self.name = name

        self.oxygen_level = self.DEFAULT_OXYGEN_LEVEL or oxygen_level
        self.starting_oxygen = self.oxygen_level

        self.catch: List[BaseFish] = []
        self.competition_points = 0
        self.has_health_issue: bool = False

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Diver name cannot be null or empty!")

        self.__name = name

    @property
    def oxygen_level(self) -> float:
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, oxygen_level: float) -> None:
        if oxygen_level < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")

        self.__oxygen_level = oxygen_level

    @property
    @abstractmethod
    def oxygen_depletion_coefficient(self) -> float: ...

    def miss(self, time_to_catch: int) -> None:
        lost_oxygen = round(self.oxygen_depletion_coefficient * time_to_catch)
        self.oxygen_level = max(0, self.oxygen_level - lost_oxygen)

    def renew_oxy(self) -> None:
        self.oxygen_level = self.starting_oxygen

    def hit(self, fish: BaseFish) -> None:
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
            return

        self.oxygen_level -= fish.time_to_catch

        self.catch.append(fish)
        self.competition_points += fish.points

    def update_health_status(self) -> None:
        self.has_health_issue = not self.has_health_issue

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}: [Name: {self.name}, "
            f"Oxygen level left: {self.oxygen_level}, Fish caught: "
            f"{len(self.catch)}, Points earned: {self.competition_points:.1f}]"
        )
