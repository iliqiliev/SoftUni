from typing import Dict
from project.computer_types import Computer


class Laptop(Computer):
    @property
    def _valid_processors(self) -> Dict[str, int]:
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

    @property
    def _max_ram(self) -> int:
        return 64

    @property
    def _nickname(self) -> str:
        return "laptop"
