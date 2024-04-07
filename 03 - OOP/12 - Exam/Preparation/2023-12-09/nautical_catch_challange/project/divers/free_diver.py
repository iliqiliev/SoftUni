from project.divers import BaseDiver


class FreeDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL: float = 120

    @property
    def oxygen_depletion_coefficient(self) -> float:
        return 0.6
