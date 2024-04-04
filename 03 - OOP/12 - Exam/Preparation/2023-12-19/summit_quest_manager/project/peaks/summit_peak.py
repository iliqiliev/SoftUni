from typing import List
from project.peaks import BasePeak


class SummitPeak(BasePeak):
    def get_recommended_gear(self) -> List[str]:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self) -> str:
        if self.elevation <= 2500:
            return "Advanced"

        return "Extreme"
