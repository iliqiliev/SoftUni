matrix_size = int(input())
matrix = [input().split(", ") for _ in range(matrix_size)]

primary_diagonal = []
secondary_diagonal = []

primary_sum = 0
secondary_sum = 0

for index in range(matrix_size):
    primary_diagonal.append(matrix[index][index])
    primary_sum += int(primary_diagonal[index])

    secondary_diagonal.append(matrix[index][matrix_size - index - 1])
    secondary_sum += int(secondary_diagonal[index])


print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {secondary_sum}")
