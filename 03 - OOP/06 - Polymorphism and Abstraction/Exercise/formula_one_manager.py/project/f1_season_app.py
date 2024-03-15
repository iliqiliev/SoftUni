from typing import Optional
from project.formula_teams import RedBullTeam, MercedesTeam


class F1SeasonApp:
    def __init__(self) -> None:
        self.red_bull_team: Optional[RedBullTeam] = None
        self.mercedes_team: Optional[MercedesTeam] = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(
        self, race_name: str, red_bull_pos: int, mercedes_pos: int
    ) -> str:

        if not all((self.red_bull_team, self.mercedes_team)):
            # pylint: disable=broad-exception-raised
            raise Exception("Not all teams have registered for the season.")

        return self.get_race_results(race_name, red_bull_pos, mercedes_pos)

    def get_race_results(
        self, race_name: str, red_bull_pos: int, mercedes_pos: int
    ) -> str:

        assert self.red_bull_team is not None
        assert self.mercedes_team is not None

        red_bull_info = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_info = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        ahead = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return (
            f"Red Bull: {red_bull_info}. Mercedes: {mercedes_info}. "
            f"{ahead} is ahead at the {race_name} race."
        )
