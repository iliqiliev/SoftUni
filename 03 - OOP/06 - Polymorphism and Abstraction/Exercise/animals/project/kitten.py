from project import Cat


class Kitten(Cat):
    _SOUND = "Meow"

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, "Female")
