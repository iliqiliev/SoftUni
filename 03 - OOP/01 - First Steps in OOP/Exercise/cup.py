class Cup:
    def __init__(self, size: int, quantity: int) -> None:
        self.size = size
        self.quantity = quantity

    def status(self) -> int:
        return self.size - self.quantity

    def fill(self, fill_amount: int) -> None:
        if fill_amount <= self.status():
            self.quantity += fill_amount
