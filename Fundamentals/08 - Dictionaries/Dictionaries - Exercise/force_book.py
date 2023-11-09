from collections import defaultdict


force_sides = defaultdict(list)

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, _, user = command.partition(" | ")

        if not any(user in users for users in force_sides.values()):
            force_sides[side].append(user)

    elif "->" in command:
        user, _, side = command.partition(" -> ")

        if not any(user in users for users in force_sides.values()):
            force_sides[side].append(user)

        else:
            for old_side, users in force_sides.items():
                if user in users:
                    force_sides[old_side].remove(user)
                    force_sides[side].append(user)
                    break

        print(f"{user} joins the {side} side!")

for side, members in force_sides.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")
