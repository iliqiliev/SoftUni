from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> str:
        return self.sound

    @property
    @abstractmethod
    def sound(self) -> str: ...


class Cat(Animal):
    @property
    def sound(self) -> str:
        return "Мяу"


class Dog(Animal):
    @property
    def sound(self) -> str:
        return "Джаф!"


class Pig(Animal):
    @property
    def sound(self) -> str:
        return "Грух"


def animal_sounds(animals: list[Animal]) -> str:
    return "\n".join(animal.make_sound() for animal in animals)


def main():
    animals = [
        Cat("Pori"),
        Pig("Singerski"),
        Dog("Rundjo"),
    ]

    print(animal_sounds(animals))


if __name__ == "__main__":
    main()
