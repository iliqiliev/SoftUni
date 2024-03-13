from project import AutoIncrementMixin


class Customer(AutoIncrementMixin):
    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return (
            f"Customer <{self.id}> {self.name}; "
            f"Address: {self.address}; Email: {self.email}"
        )
