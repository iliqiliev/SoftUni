from typing import List


class Vet:
    space = 5
    animals: List[str] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, name: str) -> str:
        if not Vet.space:
            return "Not enough space"

        Vet.space -= 1
        Vet.animals.append(name)
        self.animals.append(name)

        return f"{name} registered in the clinic"

    def unregister_animal(self, name) -> str:
        if name not in Vet.animals:
            return f"{name} not in the clinic"

        Vet.space += 1
        Vet.animals.remove(name)
        self.animals.remove(name)

        return f"{name} unregistered successfully"

    def info(self) -> str:
        return (
            f"{self.name} has {len(self.animals)} animals. "
            f"{Vet.space} space left in clinic"
        )
