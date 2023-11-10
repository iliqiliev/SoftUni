from collections import defaultdict


inventory = defaultdict(int, {"shards": 0, "fragments": 0, "motes": 0})
winner_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath",
}

winner = None

while not winner:
    bag = input().lower().split()

    for index in range(0, len(bag), 2):
        item_name = bag[index + 1]
        item_count = int(bag[index])

        inventory[item_name] += item_count

        if item_name in winner_items and inventory[item_name] >= 250:
            inventory[item_name] -= 250
            winner = winner_items[item_name]
            break

print(f"{winner} obtained!")
for item, count in inventory.items():
    print(f"{item}: {count}")
