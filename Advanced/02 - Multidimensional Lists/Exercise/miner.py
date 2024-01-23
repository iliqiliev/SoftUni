DIRECTIONS = {
    "left":  (0, -1),
    "right": (0, +1),
    "up":    (-1, 0),
    "down":  (+1, 0),
}


def move(old_position: tuple, command: str, field_size: int) -> tuple:
    change = DIRECTIONS[command]
    new_position = (old_position[0] + change[0], old_position[1] + change[1])

    if all(position in range(field_size) for position in new_position):
        return new_position

    return old_position


def main():
    field_size = int(input())
    commands = input().split()
    coal = 0
    miner = (0, 0)
    field = []

    for row_index in range(field_size):
        col = input().split()
        field.append(col)
        coal += col.count("c")

        if "s" in col:
            miner = (row_index, col.index("s"))

    for command in commands:
        field[miner[0]][miner[1]] = "*"  # replace last item

        miner = move(miner, command, field_size)
        current_item = field[miner[0]][miner[1]]

        if current_item == "c":
            coal -= 1

            if not coal:
                print(f"You collected all coal! ({miner[0]}, {miner[1]})")
                break

        elif current_item == "e":
            print(f"Game over! ({miner[0]}, {miner[1]})")
            break

    else:
        print(f"{coal} pieces of coal left. "
              f"({miner[0]}, {miner[1]})")


if __name__ == "__main__":
    main()
