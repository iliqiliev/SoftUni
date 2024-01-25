knight_moves = {
    (-2, +1),
    (-1, +2),
    (+1, +2),
    (+2, +1),
    (+2, -1),
    (+1, -2),
    (-1, -2),
    (-2, -1),
}

knights = {}
removed_knights = 0

for row_index in range(int(input())):
    line = input()

    for col_index, piece in enumerate(line):
        if piece == "K":
            knights[(row_index, col_index)] = set()

for knight, enemies in knights.items():
    knight_x, knight_y = knight

    for move_x, move_y in knight_moves:
        target = (knight_x + move_x, knight_y + move_y)

        if target in knights:
            enemies.add(target)

for _ in range(len(knights) - 1):
    baddest_knight = max(knights, key=lambda enemies: len(knights[enemies]))

    if not knights.pop(baddest_knight, None):
        break

    removed_knights += 1

    for enemies in knights.values():
        if baddest_knight in enemies:
            enemies.remove(baddest_knight)

print(removed_knights)
