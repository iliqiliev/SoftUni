from typing import List
from project import Player, NO_GUILD


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != NO_GUILD:
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for index, player in enumerate(self.players):
            if player.name == player_name:
                break

        else:
            return f"Player {player_name} is not in the guild."

        player.guild = NO_GUILD
        self.players.pop(index)

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = [
            f"Guild: {self.name}",
            *(player.player_info() for player in self.players)
        ]

        return "\n".join(result)
