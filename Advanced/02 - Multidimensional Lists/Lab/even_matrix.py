matrix = []

for _ in range(int(input())):
    matrix.append([int(num) for num in input().split(", ") if not int(num) & 1])

print(matrix)
