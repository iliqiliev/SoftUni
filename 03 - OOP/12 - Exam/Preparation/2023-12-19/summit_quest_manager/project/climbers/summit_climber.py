from project.climbers import BaseClimber
from project.peaks import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str) -> None:
        super().__init__(name, 150)

    @property
    def min_strength(self) -> float:
        return 75

    def climb(self, peak: BasePeak) -> None:
        base_strength_required = 30
        multiplier = 1.3 if peak.difficulty_level == "Advanced" else 2.5

        self.strength -= base_strength_required * multiplier

        self.conquered_peaks.append(peak.name)
