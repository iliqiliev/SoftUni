from project.animal import Animal


class Cat(Animal):  # pylint: disable=too-few-public-methods
    def meow(self) -> str:
        return "meowing..."
