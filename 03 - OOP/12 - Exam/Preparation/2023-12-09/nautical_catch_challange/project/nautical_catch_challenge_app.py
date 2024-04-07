from typing import Dict, List, Type, Union
from project.divers import BaseDiver, FreeDiver, ScubaDiver
from project.fish import BaseFish, DeepSeaFish, PredatoryFish


DiverHasDefaultOxygen = Type[Union[FreeDiver, ScubaDiver]]
FishHasDefaultTimeToCatch = Type[Union[DeepSeaFish, PredatoryFish]]


class NauticalCatchChallengeApp:
    valid_divers: Dict[str, DiverHasDefaultOxygen] = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }

    valid_fish: Dict[str, FishHasDefaultTimeToCatch] = {
        "DeepSeaFish": DeepSeaFish,
        "PredatoryFish": PredatoryFish,
    }

    def __init__(self) -> None:
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, type_: str, name: str) -> str:
        if type_ not in self.valid_divers:
            return f"{type_} is not allowed in our competition."

        if any(diver.name == name for diver in self.divers):
            return f"{name} is already a participant."

        diver_class = self.valid_divers[type_]
        diver = diver_class(name)

        self.divers.append(diver)

        return (
            f"{name} is successfully registered "
            f"for the competition as a {type_}."
        )

    def swim_into_competition(
        self, type_: str, name: str, points: float
    ) -> str:

        if type_ not in self.valid_fish:
            return f"{type_} is forbidden for chasing in our competition."

        if any(fish.name == name for fish in self.fish_list):
            return f"{name} is already permitted."

        fish_class = self.valid_fish[type_]
        fish = fish_class(name, points)

        self.fish_list.append(fish)

        return f"{name} is allowed for chasing as a {type_}."

    def _get_diver(self, name: str) -> BaseDiver:
        for diver in self.divers:
            if diver.name == name:
                return diver

        raise ValueError(f"{name} is not registered for the competition.")

    def _get_fish(self, name: str) -> BaseFish:
        for fish in self.fish_list:
            if fish.name == name:
                return fish

        raise ValueError(
            f"The {name} is not allowed to be caught in this competition."
        )

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        try:
            diver = self._get_diver(diver_name)
            fish = self._get_fish(fish_name)

        except ValueError as error:
            return str(error)

        if diver.has_health_issue:
            return (
                f"{diver_name} will not be allowed to dive, due to health issues."
            )

        if (
            diver.oxygen_level < fish.time_to_catch or
            diver.oxygen_level == fish.time_to_catch and not is_lucky
        ):
            diver.miss(fish.time_to_catch)
            result = f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            result = f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.has_health_issue = True

        return result

    def health_recovery(self) -> str:
        divers_recovered = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()

                divers_recovered += 1

        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, name: str) -> str:
        diver = self._get_diver(name)

        return "\n".join((
            f"**{name} Catch Report**",
            *(fish.fish_details() for fish in diver.catch)
        ))

    def competition_statistics(self) -> str:
        divers_info = sorted(
            filter(lambda diver: not diver.has_health_issue, self.divers),
            key=lambda diver: (
                -diver.competition_points, -len(diver.catch), diver.name
            )
        )

        result = [
            "**Nautical Catch Challenge Statistics**",
            *map(str, divers_info)
        ]

        return "\n".join(result)
