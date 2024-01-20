import sys


matrix_size = int(input())
matrix = [list(input()) for _ in range(matrix_size)]

needed_symbol = input()

for row_index in range(matrix_size):
    for col_index in range(matrix_size):
        if matrix[row_index][col_index] == needed_symbol:
            print(f"({row_index}, {col_index})")
            sys.exit()  # lazy

print(f"{needed_symbol} does not occur in the matrix")
