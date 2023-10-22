travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for command in travel_route:

    command = command.split()
    option = command[0]

    if option == "Travel":
        distance = int(command[1])

        if fuel >= distance:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")

        else:
            print("Mission failed.")
            break

    elif option == "Enemy":
        armour = int(command[1])

        if ammunition >= armour:
            ammunition -= armour
            print(f"An enemy with {armour} armour is defeated.")

        elif fuel >= armour * 2:
            fuel -= armour * 2
            print(f"An enemy with {armour} armour is outmaneuvered.")

        else:
            print("Mission failed.")
            break

    elif option == "Repair":
        restock = int(command[1])

        ammunition += restock * 2
        fuel += restock

        print(f"Ammunitions added: {restock * 2}.\n"
              f"Fuel added: {restock}.")

    elif option == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
