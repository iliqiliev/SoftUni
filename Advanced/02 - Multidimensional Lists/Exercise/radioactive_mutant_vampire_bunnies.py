MOVES = {
    "L": (0, -1),
    "R": (0, +1),
    "U": (-1, 0),
    "D": (+1, 0),
}


def in_lair(position: tuple, lair_size: tuple) -> bool:
    return (position[0] in range(lair_size[0]) and
            position[1] in range(lair_size[1]))


def mutate_bunnies(lair: list, lair_size: tuple, bunnies: set) -> list:
    for bunny_x, bunny_y in bunnies.copy():
        for move_x, move_y in MOVES.values():
            new_bunny_x = bunny_x + move_x
            new_bunny_y = bunny_y + move_y

            if in_lair((new_bunny_x, new_bunny_y), lair_size):
                lair[new_bunny_x][new_bunny_y] = "B"
                bunnies.add((new_bunny_x, new_bunny_y))

    return lair


def move_player(player: tuple, command: str) -> tuple:
    move = MOVES[command]
    return (player[0] + move[0], player[1] + move[1])


def main():
    lair_size = tuple(map(int, input().split()))
    lair = []
    bunnies = set()
    player = (0, 0)

    for row_index in range(lair_size[0]):
        lair.append(list(input()))

        for col_index, element in enumerate(lair[row_index]):
            if element == "B":
                bunnies.add((row_index, col_index))

            elif element == "P":
                lair[row_index][col_index] = "."
                player = (row_index, col_index)

    commands = input()
    status = None

    for command in commands:
        last_player = player

        player = move_player(player, command)
        lair = mutate_bunnies(lair, lair_size, bunnies)

        if not in_lair(player, lair_size):
            player = last_player
            status = "won"
            break

        if lair[player[0]][player[1]] == "B":
            status = "dead"
            break

    for row in lair:
        print("".join(row))
    print(f"{status}: {player[0]} {player[1]}")


if __name__ == "__main__":
    main()
