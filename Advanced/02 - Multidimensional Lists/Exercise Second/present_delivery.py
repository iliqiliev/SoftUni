directions = {
    "left":  (0, -1),
    "right": (0, +1),
    "up":    (-1, 0),
    "down":  (+1, 0),
}


def santa_visit(factions: dict, santa: tuple, presents: int, generous=False) -> int:
    for name, members in factions.items():
        if presents and santa in members:
            members.remove(santa)

            if name == "V" or generous:  # all kids case
                presents -= 1

            elif name == "C":
                for direction in directions.values():
                    santa_generous = (santa[0] + direction[0], santa[1] + direction[1])

                    all_kids = {name: factions[name] for name in "XV"}
                    presents = santa_visit(all_kids, santa_generous, presents, True)

    return presents


def print_matrix(matrix_size: int, factions: dict, santa: tuple) -> None:
    matrix = [["-"] * matrix_size for _ in range(matrix_size)]

    for name, members in factions.items():
        for member in members:
            matrix[member[0]][member[1]] = name

    matrix[santa[0]][santa[1]] = "S"

    for row in matrix:
        print(*row)


def main():
    factions = {
        "V": set(),
        "X": set(),
        "C": set(),
    }

    presents = int(input())
    matrix_size = int(input())

    santa = (0, 0)

    for row_index in range(matrix_size):
        row_data = input().split()

        for col_index, char in enumerate(row_data):
            if char in factions:
                factions[char].add((row_index, col_index))

            elif char == "S":
                santa = (row_index, col_index)

    total_nice_kids = len(factions["V"])

    while presents:
        move = directions.get(input(), None)
        if not move:
            break

        santa = (santa[0] + move[0], santa[1] + move[1])
        presents = santa_visit(factions, santa, presents)

    else:
        if factions["V"]:
            print("Santa ran out of presents!")

    print_matrix(matrix_size, factions, santa)  # f matrices

    if factions["V"]:
        print(f"No presents for {len(factions['V'])} nice kid/s.")

    else:
        happy_kids = total_nice_kids - len(factions['V'])
        print(f"Good job, Santa! {happy_kids} happy nice kid/s.")


if __name__ == "__main__":
    main()
