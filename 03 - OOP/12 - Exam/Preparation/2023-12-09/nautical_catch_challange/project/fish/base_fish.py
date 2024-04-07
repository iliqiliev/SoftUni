from abc import ABC


class BaseFish(ABC):
    DEFAULT_TIME_TO_CATCH: int = 0

    def __init__(
        self, name: str, points: float, time_to_catch: int = 0
    ) -> None:

        self.name = name
        self.points = points
        self.time_to_catch = self.DEFAULT_TIME_TO_CATCH or time_to_catch

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Fish name should be determined!")

        self.__name = name

    @property
    def points(self) -> float:
        return self.__points

    @points.setter
    def points(self, points: float) -> None:
        if not 1 <= points <= 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")

        self.__points = points

    def fish_details(self) -> str:
        return (
            f"{self.__class__.__name__}: {self.name} [Points: {self.points}, "
            f"Time to Catch: {self.time_to_catch} seconds]"
        )
