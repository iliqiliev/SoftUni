from typing import Dict


class Shop:
    def __init__(self, name: str, type_: str, capacity: int) -> None:
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.items: Dict[str, int] = {}

    @classmethod
    def small_shop(cls, name: str, type_: str) -> "Shop":
        SMALL_SHOP_SIZE = 10

        return cls(name, type_, SMALL_SHOP_SIZE)

    def add_item(self, item_name: str) -> str:
        if sum(self.items.values()) >= self.capacity:
            return "Not enough capacity in the shop"

        self.items[item_name] = self.items.get(item_name, 0) + 1

        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if self.items.get(item_name, 0) < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if not self.items[item_name]:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
