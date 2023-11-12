from collections import defaultdict


def show_players(players: dict) -> None:
    def skill_sorting_key(player_info: tuple) -> tuple:
        name, skills = player_info
        # this way the function works if skills is a int - when sorting the positions
        skills = skills.values() if isinstance(skills, dict) else [skills]

        # sort by descending total skill and ascending name
        return (-sum(skills), name)

    for name, positions in sorted(players.items(), key=skill_sorting_key):
        print(f"{name}: {sum(positions.values())} skill")

        for position, skill in sorted(positions.items(), key=skill_sorting_key):
            print(f"- {position} <::> {skill}")


def duel(duellist: str, opponent: str, players: dict) -> None:
    if {duellist, opponent}.issubset(players.keys()):
        # intersection of two sets
        common_positions = players[duellist].keys() & players[opponent].keys()

        for position in common_positions:
            # if the player is removed we shouldn't try to access him again so we break
            if players[duellist][position] > players[opponent][position]:
                players.pop(opponent)
                break

            if players[duellist][position] < players[opponent][position]:
                players.pop(duellist)
                break


def main():
    players = defaultdict(dict)

    while True:
        command = input()
        if command == "Season end":
            break

        if "vs" in command:
            duellist, opponent = command.split(" vs ")
            duel(duellist, opponent, players)

        elif "->" in command:
            player, position, skill = command.split(" -> ")
            skill = int(skill)

            players[player][position] = max(skill, players[player].get(position, 0))

    show_players(players)


if __name__ == "__main__":
    main()
