from typing import Dict, List, Type, Union
from project.climbers import BaseClimber, ArcticClimber, SummitClimber
from project.peaks import BasePeak, ArcticPeak, SummitPeak


ClimberHasDefaultStrength = Type[Union[ArcticClimber, SummitClimber]]


class SummitQuestManagerApp:
    valid_climbers: Dict[str, ClimberHasDefaultStrength] = {
        "ArcticClimber": ArcticClimber,
        "SummitClimber": SummitClimber
    }

    valid_peaks: Dict[str, Type[BasePeak]] = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak
    }

    def __init__(self) -> None:
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, type_: str, name: str) -> str:
        if type_ not in self.valid_climbers:
            return f"{type_} doesn't exist in our register."

        if any(climber.name == name for climber in self.climbers):
            return f"{name} has been already registered."

        climber_class = self.valid_climbers[type_]
        climber = climber_class(name)

        self.climbers.append(climber)

        return f"{name} is successfully registered as a {type_}."

    def peak_wish_list(self, type_: str, name: str, elevation: int) -> str:
        if type_ not in self.valid_peaks:
            return f"{type_} is an unknown type of peak."

        peak_class = self.valid_peaks[type_]
        peak = peak_class(name, elevation)

        self.peaks.append(peak)

        return f"{name} is successfully added to the wish list as a {type_}."

    def _get_climber(self, name: str) -> BaseClimber:
        for climber in self.climbers:
            if climber.name == name:
                return climber

        raise ValueError(f"Climber {name} is not registered yet.")

    def _get_peak(self, name: str) -> BasePeak:
        for peak in self.peaks:
            if peak.name == name:
                return peak

        raise ValueError(f"Peak {name} is not part of the wish list.")

    def check_gear(
        self, climber_name: str, peak_name: str, gear: List[str]
    ) -> str:

        climber = self._get_climber(climber_name)
        peak = self._get_peak(peak_name)

        missing_gear = sorted(set(peak.get_recommended_gear()).difference(gear))

        if missing_gear:
            climber.is_prepared = False

            return (
                f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join(missing_gear)}."
            )

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        try:
            climber = self._get_climber(climber_name)
            peak = self._get_peak(peak_name)

        except ValueError as error:
            return str(error)

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()

            return (
                f"{climber_name} needs more strength to climb {peak_name} "
                "and is therefore taking some rest."
            )

        climber.climb(peak)

        return (
            f"{climber_name} conquered {peak_name} "
            f"whose difficulty level is {peak.difficulty_level}."
        )

    def get_statistics(self) -> str:
        total_conquered_peaks = len(
            set(
                peak
                for climber in self.climbers
                for peak in climber.conquered_peaks
            )
        )

        climbers_sorted = sorted(
            filter(lambda climber: climber.conquered_peaks, self.climbers),
            key=lambda climber: (
                -len(climber.conquered_peaks), climber.name
            )
        )

        result = [
            f"Total climbed peaks: {total_conquered_peaks}",
            "**Climber's statistics:**",
            *map(str, climbers_sorted)
        ]

        return "\n".join(result)
