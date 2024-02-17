matrix_size = 5
matrix_range = range(matrix_size)

targets = set()
targets_hit = []

gunman = (0, 0)
directions = {
    "up":    (-1, 0),
    "down":  (+1, 0),
    "left":  (0, -1),
    "right": (0, +1),
}

for row_index in matrix_range:
    row_data = input().split()

    if "A" in row_data:
        gunman = (row_index, row_data.index("A"))

    for col_index, char in enumerate(row_data):
        if char == "x":
            targets.add((row_index, col_index))


for _ in range(int(input())):
    _, move, *steps = input().split()
    move = directions[move]

    if steps:  # move
        steps = int(steps[0])
        move_try = (gunman[0] + move[0] * steps, gunman[1] + move[1] * steps)

        if (
            move_try[0] in matrix_range
            and move_try[1] in matrix_range
            and move_try not in targets
        ):
            gunman = move_try

    else:  # shoot
        potential = ((gunman[0] + move[0] * step, gunman[1] + move[1] * step)
                     for step in matrix_range)

        for target in potential:
            if target in targets:
                targets.remove(target)
                targets_hit.append(f"[{target[0]}, {target[1]}]")
                break

        if not targets:
            print(f"Training completed! All {len(targets_hit)} targets hit.")
            break

else:
    print(f"Training not completed! {len(targets)} targets left.")

print("\n".join(targets_hit))
