from typing import Dict
from project.computer_types import Computer


class DesktopComputer(Computer):
    @property
    def _valid_processors(self) -> Dict[str, int]:
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800,
        }

    @property
    def _max_ram(self) -> int:
        return 128

    @property
    def _nickname(self) -> str:
        return "desktop computer"
