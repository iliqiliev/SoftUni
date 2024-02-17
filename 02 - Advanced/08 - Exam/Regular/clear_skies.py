JET = "J"
ENEMY = "E"
REPAIR = "R"
EMPTY = "-"
INITIAL_ARMOUR = 300

DIRECTIONS = {
    "up":    (-1, 0),
    "down":  (+1, 0),
    "left":  (0, -1),
    "right": (0, +1),
}


jet_position = (0, 0)
enemy_jets = 0

matrix_size = int(input())
matrix = []

for row_index in range(matrix_size):
    row_data = list(input())

    for col_index, char in enumerate(row_data):

        if char == ENEMY:
            enemy_jets += 1

        elif char == JET:
            jet_position = (row_index, col_index)

    matrix.append(row_data)

armour = INITIAL_ARMOUR

while enemy_jets:
    matrix[jet_position[0]][jet_position[1]] = EMPTY
    move = DIRECTIONS[input()]

    jet_position = (
        jet_position[0] + move[0],
        jet_position[1] + move[1]
    )

    target_cell = matrix[jet_position[0]][jet_position[1]]
    matrix[jet_position[0]][jet_position[1]] = JET

    if target_cell == EMPTY:
        continue

    if target_cell == ENEMY:
        enemy_jets -= 1

        if not enemy_jets:
            continue

        armour -= 100

        if armour <= 0:
            print(
                "Mission failed, your jetfighter was shot down!",
                f"Last coordinates [{jet_position[0]}, {jet_position[1]}]!"
            )
            break

    elif target_cell == REPAIR:
        armour = INITIAL_ARMOUR


else:
    print("Mission accomplished, you neutralized the aerial threat!")

for row in matrix:
    print("".join(row))
