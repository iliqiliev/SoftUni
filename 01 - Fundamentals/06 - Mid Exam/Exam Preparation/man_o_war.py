def main():

    pirate_ship = [int(number) for number in input().split(">")]
    warship = [int(number) for number in input().split(">")]
    max_hp_capacity = int(input())

    command = input().split()
    while command[0] != "Retire":

        option = command[0]
        if option == "Fire":
            # the first index is the option already
            index, damage = map(int, command[1:])

            if fire(warship, index, damage):
                print("You won! The enemy ship has sunken.")
                break

        elif option == "Defend":
            start_index, end_index, damage = map(int, command[1:])

            if defend(pirate_ship, start_index, end_index, damage):
                print("You lost! The pirate ship has sunken.")
                break

        elif option == "Repair":
            index, health = map(int, command[1:])
            repair(pirate_ship, index, health, max_hp_capacity)

        elif option == "Status":
            status(pirate_ship, max_hp_capacity)

        command = input().split()

    else:
        print(f"Pirate ship status: {sum(pirate_ship)}\n"
              f"Warship status: {sum(warship)}")


def valid_index(ship: list, index: int, index2=0) -> bool:
    # works with one or two indices by giving index2 a default value
    if (0 <= index < len(ship)) and (0 <= index2 < len(ship)):
        return True

    return False


def fire(ship: list, index: int, damage: int) -> bool:

    if valid_index(ship, index):
        ship[index] -= damage

        if ship[index] <= 0:
            return True

    return False


def defend(ship: list, start: int, end: int, damage: int) -> bool:

    if valid_index(ship, start, end):
        for section in range(start, end + 1):
            ship[section] -= damage

            if ship[section] <= 0:
                return True
            
    return False


def repair(ship: list, index: int, health: int, max_hp: int) -> None:

    if valid_index(ship, index):
        # don't go over max hp
        ship[index] = min(ship[index] + health, max_hp)


def status(ship: list, max_hp: int) -> int:

    damaged = sum(1 for section in ship if section < (0.2 * max_hp))
    print(f"{damaged} sections need repair.")

    return damaged


if __name__ == "__main__":
    main()
