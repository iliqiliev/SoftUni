from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    _MIN_BUDGET = 1_000_000

    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int) -> None:
        if budget < self._MIN_BUDGET:
            raise ValueError(
                "F1 is an expensive sport, find more sponsors!"
            )
        self.__budget = budget

    @property
    @abstractmethod
    def sponsors(self) -> Dict[str, Dict[int, int]]: ...

    @property
    def expenses(self) -> int: ...

    def calculate_revenue_after_race(self, race_position: int) -> str:
        revenue = 0

        for sponsor_info in self.sponsors.values():
            for position, money in sponsor_info.items():
                if race_position <= position:
                    revenue += money
                    break

        revenue -= self.expenses
        self.budget += revenue

        return (
            f"The revenue after the race is {revenue}$. "
            f"Current budget {self.budget}$"
        )
