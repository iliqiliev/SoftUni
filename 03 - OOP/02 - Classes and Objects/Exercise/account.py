from typing import Union


class Account:
    def __init__(self, _id: int, name: str, balance: float = 0) -> None:
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: float) -> float:
        self.balance += amount

        return self.balance

    def debit(self, amount: float) -> Union[str, float]:
        if self.balance < amount:
            return "Amount exceeded balance"

        self.balance -= amount

        return self.balance

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"
