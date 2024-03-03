from project.animal import Animal


class Dog(Animal):  # pylint: disable=too-few-public-methods
    def bark(self) -> str:
        return "barking..."
