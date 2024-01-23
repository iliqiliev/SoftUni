rows, cols = map(int, input().split())

matrix = [[int(num) for num in input().split()] for _ in range(rows)]

biggest_sum = float("-inf")
biggest_matrix = [0, 0, 0]
submatrix_size = 3

for row_index in range(rows - (submatrix_size - 1)):
    for col_index in range(cols - (submatrix_size - 1)):
        submatrix = []
        submatrix_sum = 0

        for sub_row in range(row_index, row_index + submatrix_size):
            submatrix_row = matrix[sub_row][col_index:col_index + submatrix_size]
            submatrix.append(submatrix_row)
            submatrix_sum += sum(submatrix_row)

        if submatrix_sum > biggest_sum:
            biggest_matrix = submatrix
            biggest_sum = submatrix_sum

print(f"Sum = {biggest_sum}")
for sub_row in range(submatrix_size):
    print(*biggest_matrix[sub_row])
