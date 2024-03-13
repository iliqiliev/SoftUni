from project import AutoIncrementMixin


class Equipment(AutoIncrementMixin):
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
