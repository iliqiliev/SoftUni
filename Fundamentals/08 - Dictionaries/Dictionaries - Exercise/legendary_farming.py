from collections import defaultdict


inventory = defaultdict(int)
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
print(f"shards: {inventory.pop('shards', 0)}")
print(f"fragments: {inventory.pop('fragments', 0)}")
print(f"motes: {inventory.pop('motes', 0)}")
for item, count in inventory.items():
    print(f"{item}: {count}")
