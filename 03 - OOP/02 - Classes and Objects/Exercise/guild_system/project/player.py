from typing import Dict


NO_GUILD = "Unaffiliated"


class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str, int] = {}
        self.guild = NO_GUILD

    def add_skill(self, name: str, mana_cost: int) -> str:
        if name in self.skills:
            return "Skill already added"

        self.skills[name] = mana_cost

        return f"Skill {name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        result = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
            *(
                f"==={name} - {mana_cost}"
                for name, mana_cost in self.skills.items()
            )
        ]

        return "\n".join(result)
