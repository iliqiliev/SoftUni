from project.climbers import BaseClimber
from project.peaks import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str) -> None:
        super().__init__(name, 200)

    @property
    def min_strength(self) -> float:
        return 100

    def climb(self, peak: BasePeak) -> None:
        base_strength_required = 20
        multiplier = 2 if peak.difficulty_level == "Extreme" else 1.5

        self.strength -= base_strength_required * multiplier

        self.conquered_peaks.append(peak.name)
