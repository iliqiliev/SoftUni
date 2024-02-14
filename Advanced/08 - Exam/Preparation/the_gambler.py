from typing import Tuple


DIRECTIONS = {
    "up":    (-1, 0),
    "down":  (+1, 0),
    "left":  (0, -1),
    "right": (0, +1),
}


def move_gambler(
    gambler: Tuple[int, int], command: str, matrix_size: int
) -> Tuple[int, int]:
    move = DIRECTIONS[command]

    gambler = (
        gambler[0] + move[0],
        gambler[1] + move[1]
    )

    if not all(0 <= axis < matrix_size for axis in gambler):
        raise IndexError

    return gambler


def main():
    matrix_size = int(input())
    money = 100

    gambler = (0, 0)
    matrix = []

    for row_index in range(matrix_size):
        row_data = list(input())

        if "G" in row_data:
            col_index = row_data.index("G")

            gambler = (row_index, col_index)
            row_data[col_index] = "-"

        matrix.append(row_data)

    command = input()
    jackpot = False

    while command != "end" and not jackpot:
        try:
            gambler = move_gambler(gambler, command, matrix_size)

        except IndexError:
            break

        position_data = matrix[gambler[0]][gambler[1]]
        matrix[gambler[0]][gambler[1]] = "-"

        if position_data == "W":
            money += 100

        elif position_data == "P":
            money -= 200

            if money < 1:
                break

        elif position_data == "J":
            jackpot = True
            money += 100000
            continue

        command = input()

    else:
        matrix[gambler[0]][gambler[1]] = "G"

        if jackpot:
            print("You win the Jackpot!")

        print(f"End of the game. Total amount: {money}$")

        for row in matrix:
            print("".join(row))

        return

    print("Game over! You lost everything!")


if __name__ == "__main__":
    main()
