from typing import List
from project import DVD


class Customer:
    def __init__(self, name: str, age: int, id_: int) -> None:
        self.name = name
        self.age = age
        self.id = id_
        self.rented_dvds: List[DVD] = []

    def __repr__(self) -> str:
        return (
            f"{self.id}: {self.name} of age {self.age} has "
            f"{len(self.rented_dvds)} rented DVD's "
            f"({', '.join(dvd.name for dvd in self.rented_dvds)})"
        )
