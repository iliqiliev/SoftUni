class Animal:
    _DEFAULT_MONEY_FOR_CARE = 0

    def __init__(self, name: str, gender: str, age: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = self._DEFAULT_MONEY_FOR_CARE

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
