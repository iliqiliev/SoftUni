class Car:  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, model: str, engine: str) -> None:
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self) -> str:
        return f"This is {self.name} {self.model} with engine {self.engine}"
