from collections import defaultdict


def plunder(cities_info: dict, town: str, deaths: int, loot: int) -> dict:

    cities_info[town]["population"] -= deaths
    cities_info[town]["gold"] -= loot
    print(f"{town} plundered! {loot} gold stolen, {deaths} citizens killed.")

    if cities_info[town]["population"] <= 0 or cities_info[town]["gold"] <= 0:
        print(f"{town} has been wiped off the map!")
        cities_info.pop(town)

    return cities_info


def prosper(cities_info: dict, town: str, given_gold: int) -> dict:

    if given_gold < 0:
        print("Gold added cannot be a negative number!")
        return cities_info

    cities_info[town]["gold"] += given_gold
    print(f"{given_gold} gold added to the city treasury. "
          f"{town} now has {cities_info[town]['gold']} gold.")

    return cities_info


def main():

    targets = defaultdict(lambda: defaultdict(int))
    commands = {
        "Plunder": plunder,
        "Prosper": prosper,
    }

    while True:
        command = input().split("||")
        if len(command) != 3:
            break

        city, population, gold = command
        targets[city]["population"] += int(population)
        targets[city]["gold"] += int(gold)

    while True:
        command, *arguments = input().split("=>")
        if command not in commands:
            break

        # left stripping "-" to account for negative numbers
        arguments = [int(arg) if arg.lstrip("-").isdigit() else arg
                     for arg in arguments]
        commands[command](targets, *arguments)

    if targets:
        print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
        for city, city_info in targets.items():
            print(f"{city} -> Population: {city_info['population']} citizens, "
                  f"Gold: {city_info['gold']} kg")

    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


if __name__ == "__main__":
    main()
