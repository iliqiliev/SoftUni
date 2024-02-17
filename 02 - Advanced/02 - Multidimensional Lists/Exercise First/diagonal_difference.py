matrix_size = int(input())
primary_sum = secondary_sum = 0

for index in range(matrix_size):
    row_data = input().split()

    primary_sum += int(row_data[index])
    secondary_sum += int(row_data[matrix_size - index - 1])

print(abs(primary_sum - secondary_sum))
