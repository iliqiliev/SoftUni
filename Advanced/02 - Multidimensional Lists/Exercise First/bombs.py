from itertools import product


matrix_size = int(input())
matrix = [[int(num) for num in input().split()]
          for _ in range(matrix_size)]

bomb_coordinates = [tuple(map(int, pair.split(",")))
                    for pair in input().split()]

for x, y in bomb_coordinates:
    if matrix[x][y] < 1:
        continue

    bomb = matrix[x][y]   # cartesian product
    for delta_x, delta_y in product(range(-1, 2), repeat=2):
        blast_x = x + delta_x
        blast_y = y + delta_y

        if (blast_x in range(matrix_size) and
            blast_y in range(matrix_size) and
                matrix[blast_x][blast_y] > 0):
            matrix[blast_x][blast_y] -= bomb

alive_cells = cells_sum = 0
for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            cells_sum += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {cells_sum}")
for row in matrix:
    print(*row)
