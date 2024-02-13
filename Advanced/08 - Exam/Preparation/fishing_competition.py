DIRECTIONS = {
    "up":    (-1, 0),
    "down":  (+1, 0),
    "left":  (0, -1),
    "right": (0, +1),
}


matrix_size = int(input())
matrix_range = range(matrix_size)

fish_caught = 0
fish_quota = 20

fisher = (0, 0)
matrix = []

for row_index in matrix_range:
    row_data = list(input())

    if "S" in row_data:
        col_index = row_data.index("S")

        fisher = (row_index, col_index)
        row_data[col_index] = "-"

    matrix.append(row_data)

command = input()
while command != "collect the nets":

    move = DIRECTIONS[command]
    fisher = (
        (fisher[0] + move[0]) % matrix_size,
        (fisher[1] + move[1]) % matrix_size
    )

    position_data = matrix[fisher[0]][fisher[1]]

    if position_data.isdecimal():
        fish_caught += int(position_data)
        matrix[fisher[0]][fisher[1]] = "-"

    elif position_data == "W":
        print(
            "You fell into a whirlpool!",
            "The ship sank and you lost the fish you caught.",
            f"Last coordinates of the ship: [{fisher[0]},{fisher[1]}]"
        )
        break

    command = input()

else:
    matrix[fisher[0]][fisher[1]] = "S"

    if fish_caught >= fish_quota:
        print("Success! You managed to reach the quota!")

    else:
        print(
            "You didn't catch enough fish and didn't reach the quota!",
            f"You need {fish_quota - fish_caught} tons of fish more."
        )

    if fish_caught:
        print(f"Amount of fish caught: {fish_caught} tons.")

    for row in matrix:
        print("".join(row))
