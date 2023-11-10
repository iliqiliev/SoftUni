from collections import defaultdict


force_sides = defaultdict(list)

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")

        # if the user isn't in any of the force sides
        if not any(user in users for users in force_sides.values()):
            force_sides[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")

        # change the side if the user already has side
        for users in force_sides.values():
            if user in users:
                users.remove(user)
                force_sides[side].append(user)
                break
        # else add it to the side
        else:
            force_sides[side].append(user)

        print(f"{user} joins the {side} side!")

for side, members in force_sides.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")
