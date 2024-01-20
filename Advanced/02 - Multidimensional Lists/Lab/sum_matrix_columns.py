rows, cols = (int(num) for num in input().split(", "))

column_sums = [0] * cols

for _ in range(rows):
    row = [int(num) for num in input().split()]
    
    for column_index, number in enumerate(row):
        column_sums[column_index] += number

print(*column_sums, sep="\n")
