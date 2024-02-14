from collections import defaultdict
from typing import Tuple


def team_lineup(*player_info: Tuple[str, str]) -> str:
    countries_info = defaultdict(list)

    for player, country in player_info:
        countries_info[country].append(player)

    sorted_players = sorted(
        countries_info.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )

    result = (
        f"{country}:\n" +
        '\n'.join(f"  -{player}" for player in players)
        for country, players in sorted_players
    )

    return "\n".join(result)
