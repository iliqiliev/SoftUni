# pyright: reportGeneralTypeIssues=false
rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

while True:
    command, *indices = input().split()
    if command == "END":
        break

    valid_input = (command == "swap" and len(indices) == 4)
    if valid_input:
        indices = tuple(int(index) for index in indices)

    valid_indices = (
        valid_input and
        all(index >= 0 for index in indices) and
        all(row_index in range(rows) for row_index in (indices[0], indices[2])) and
        all(col_index in range(cols) for col_index in (indices[1], indices[3]))
    )

    if valid_indices:
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for row_index in range(rows):
            print(*matrix[row_index])

    else:
        print("Invalid input!")
