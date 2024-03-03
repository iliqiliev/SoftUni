from project.food import Food

class Fruit(Food):  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, expiration_date: str) -> None:
        self.name = name
        super().__init__(expiration_date)
