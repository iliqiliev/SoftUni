class Pokemon:  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def pokemon_details(self) -> str:
        return f"{self.name} with health {self.health}"
