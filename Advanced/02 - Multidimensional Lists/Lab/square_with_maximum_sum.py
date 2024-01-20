rows, cols = (int(num) for num in input().split(", "))

matrix = [[int(num) for num in input().split(", ")] for _ in range(rows)]
submatrix_max_sum = float("-inf")
submatrix_max = (0, 0)

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        submatrix = (
            (matrix[row_index][col_index], matrix[row_index][col_index + 1]),
            (matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1])
        )

        submatrix_sum = sum(sum(row) for row in submatrix)

        if submatrix_sum > submatrix_max_sum:
            submatrix_max_sum = submatrix_sum
            submatrix_max = submatrix

print(*submatrix_max[0])
print(*submatrix_max[1])
print(submatrix_max_sum)
