matrix_size = int(input())
diagonal_sum = 0

for index in range(matrix_size):
    diagonal_sum += int(input().split()[index])

print(diagonal_sum)
