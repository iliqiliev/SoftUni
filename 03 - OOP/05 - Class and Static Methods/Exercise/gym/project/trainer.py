from project import AutoIncrementMixin


class Trainer(AutoIncrementMixin):
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
