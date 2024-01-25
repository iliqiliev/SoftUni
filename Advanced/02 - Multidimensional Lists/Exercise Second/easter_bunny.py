bunny_original = [0, 0]
matrix_size = int(input())
matrix = []

directions = {
    "up":    {"move": (-1, 0), "eggs": float('-inf'), "path": []},
    "down":  {"move": (+1, 0), "eggs": float('-inf'), "path": []},
    "left":  {"move": (0, -1), "eggs": float('-inf'), "path": []},
    "right": {"move": (0, +1), "eggs": float('-inf'), "path": []},
}

for row_index in range(matrix_size):
    matrix.append(input().split())

    if "B" in matrix[row_index]:
        bunny_original = [row_index, matrix[row_index].index("B")]

for direction in directions.values():
    bunny = bunny_original.copy()

    while True:
        bunny[0] += direction["move"][0]
        bunny[1] += direction["move"][1]

        if (
            not (0 <= bunny[0] < matrix_size and 0 <= bunny[1] < matrix_size)
            or matrix[bunny[0]][bunny[1]] == "X"
        ):
            break

        if direction["eggs"] == float('-inf'):
            direction["eggs"] = 0
            # "Your task is to collect as many eggs as possible."
            #                                       -SoftUni

        direction["eggs"] += int(matrix[bunny[0]][bunny[1]])
        direction["path"].append(str(bunny))

best_path = max(directions, key=lambda eggs: directions[eggs]["eggs"])

print(best_path)
print("\n".join(directions[best_path]["path"]))
print(directions[best_path]["eggs"])
