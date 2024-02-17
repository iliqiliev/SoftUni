neighborhood = [int(house) for house in input().split("@")]
neighborhood_size = len(neighborhood) - 1
current_index = 0

command = input()
while command != "Love!":

    jump_amount = int(command.split()[1])
    current_index += jump_amount

    if current_index > neighborhood_size:
        current_index = 0

    if neighborhood[current_index] <= 0:
        print(f"Place {current_index} already had Valentine's day.")

    elif 0 < neighborhood[current_index] <= 2:
        print(f"Place {current_index} has Valentine's day.")

    neighborhood[current_index] -= 2
    command = input()


print(f"Cupid's last position was {current_index}.")
missed_houses = sum(1 for house in neighborhood if house > 0)

if missed_houses:
    print(f"Cupid has failed {missed_houses} places.")

else:
    print("Mission was successful.")
