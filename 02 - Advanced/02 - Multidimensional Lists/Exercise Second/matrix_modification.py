matrix_range = range(int(input()))
matrix = [[int(num) for num in input().split()]
          for _ in matrix_range]

while True:
    command, *indices = input().split()

    if not indices:
        for row in matrix:
            print(*row)

        break

    row, col, value = map(int, indices)

    if row not in matrix_range or col not in matrix_range:
        print("Invalid coordinates")
        continue

    if command == "Subtract":
        value *= -1

    matrix[row][col] += value
