from typing import Union


class Inventory:

    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.items = []

    # SoftUni please update the antique Python 3.6
    def add_item(self, item: str) -> Union[None, str]:
        if len(self.items) < self.__capacity:
            self.items.append(item)

        else:
            return "not enough room in the inventory"

    def get_capacity(self) -> int:
        return self.__capacity

    def __str__(self) -> str:
        return (f"Items: {', '.join(self.items)}.\n"
                f"Capacity left: {self.__capacity - len(self.items)}")