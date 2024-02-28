from typing import Union


class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def defend(self, damage: int) -> Union[None, str]:
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

        return None

    def heal(self, amount: int) -> None:
        self.health += amount
