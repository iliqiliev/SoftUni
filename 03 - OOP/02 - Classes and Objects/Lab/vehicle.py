from typing import List


class Vehicle:  # pylint: disable=too-few-public-methods
    def __init__(self, mileage: int, max_speed: int = 150) -> None:
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: List[str] = []
