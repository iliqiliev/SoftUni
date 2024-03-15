from abc import ABC


class Animal(ABC):
    _SOUND: str = ""

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def make_sound(cls) -> str:
        return cls._SOUND

    def __repr__(self) -> str:
        return (
            f"This is {self.name}. {self.name} is a {self.age} "
            f"year old {self.gender} {self.__class__.__name__}"
        )
