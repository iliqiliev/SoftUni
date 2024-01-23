rows, cols = map(int, input().split())
start = ord("a")

palindrome_matrix = [
    [
        chr(row_code) + chr(row_code + col_code) + chr(row_code)
        for col_code in range(cols)
    ]
    for row_code in range(start, start + rows)
]

for row_index in range(rows):
    print(*palindrome_matrix[row_index])
