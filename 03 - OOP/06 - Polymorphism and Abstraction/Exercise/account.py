from typing import List


class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    def handle_transaction(self, amount: int) -> str:
        if (self.amount + amount) < 0:
            raise ValueError("sorry cannot go in debt!")

        self.amount += amount
        self._transactions.append(amount)

        return f"New balance: {self.amount}"

    def add_transaction(self, amount: int) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    @property
    def balance(self) -> int:
        return self.amount

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:  # SoftUni using repr properly, WOW
        return f"Account({self.owner}, {self.amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index: int) -> int:
        return self._transactions[index]

    def __eq__(self, other: "Account") -> bool:
        return self.amount == other.amount

    def __ge__(self, other: "Account") -> bool:
        return self.amount >= other.amount

    def __gt__(self, other: "Account") -> bool:
        return self.amount > other.amount

    def __add__(self, other: "Account") -> "Account":
        new_name = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_transactions = self._transactions + other._transactions

        new_account = Account(new_name, new_amount)
        new_account._transactions = new_transactions

        return new_account
