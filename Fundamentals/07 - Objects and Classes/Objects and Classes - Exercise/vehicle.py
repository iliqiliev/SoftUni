from typing import Union


class Vehicle:

    def __init__(self, type: str, model: str, price: int, owner=None) -> None:
        # nice name for a variable, SoftUni
        # fails Judge automated tests if type is renamed
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str) -> str:
        if self.owner:
            return "Car already sold"

        else:
            if money >= self.price:
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

            else:
                return "Sorry, not enough money"

    def sell(self) -> Union[None, str]:
        if self.owner:
            self.owner = None

        else:
            return "Vehicle has no owner"

    def __str__(self) -> str:
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"

        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
