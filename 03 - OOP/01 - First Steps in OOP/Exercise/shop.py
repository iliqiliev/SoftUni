from typing import List


class Shop:  # pylint: disable=too-few-public-methods
    def __init__(self, name: str, items: List[str]) -> None:
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        return len(self.items)
