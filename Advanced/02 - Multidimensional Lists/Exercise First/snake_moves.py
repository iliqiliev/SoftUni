rows, cols = map(int, input().split())
string = input()

snake = string * (rows * cols // len(string) + 1)

for row in range(rows):
    current_part = snake[row * cols:(row + 1) * cols]

    if not row % 2:
        print(current_part)

    else:
        print(current_part[::-1])
