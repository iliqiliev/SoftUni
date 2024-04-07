from project.divers import BaseDiver


class ScubaDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL: float = 540

    @property
    def oxygen_depletion_coefficient(self) -> float:
        return 0.3
