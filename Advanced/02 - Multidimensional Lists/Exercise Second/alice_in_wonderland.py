territory_range = range(int(input()))
territory = []

rabbit_hole = [0, 0]
alice = [0, 0]

tea = 0
directions = {
    "left":  (0, -1),
    "right": (0, +1),
    "up":    (-1, 0),
    "down":  (+1, 0),
}

for row_index in territory_range:
    row_data = input().split()

    if "A" in row_data:
        alice = [row_index, row_data.index("A")]
        row_data[alice[1]] = "*"

    territory.append(row_data)

while tea < 10:
    move = directions[input()]
    alice[0] += move[0]
    alice[1] += move[1]

    if alice[0] not in territory_range or alice[1] not in territory_range:
        break

    find = territory[alice[0]][alice[1]]
    territory[alice[0]][alice[1]] = "*"

    if find.isdigit():
        tea += int(find)

    elif find == "R":
        break

else:
    print("She did it! She went to the party.")

if tea < 10:
    print("Alice didn't make it to the tea party.")

for row in territory:
    print(*row)
