group_size = int(input())
adventure_length_days = int(input())
coins = 0

for day in range(1, adventure_length_days + 1):

    if not day % 10:  # every 10th day
        group_size -= 2
    if not day % 15:
        group_size += 5
        coins -= (group_size * 2)

    coins += 50 - (group_size * 2)

    if not day % 3:
        coins -= (group_size * 3)
    if not day % 5:
        coins += (group_size * 20)

companion_coins = int(coins / group_size)

print(f"{group_size} companions received {companion_coins} coins each.")