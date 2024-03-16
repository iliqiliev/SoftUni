from abc import ABC


class BaseDuck(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def quack() -> str:
        return "Quack"

    def walk(self) -> str:
        return f"{self.name} walks forward..."


class Duck(BaseDuck):
    def fly(self) -> str:
        return f"{self.name} flies towards the sunrise!"


class RobotDuck(BaseDuck):
    _MAX_HEIGHT = 50

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.height = 0

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        self.__height = min(height, self._MAX_HEIGHT)

    @staticmethod
    def quack() -> str:
        return "Quack, beep-boop"

    def fly(self, height: int) -> str:
        self.height = height

        return (
            f"{self.name} tries to fly at {height}m. "
            f"He flies at {self.height}m!"
        )
