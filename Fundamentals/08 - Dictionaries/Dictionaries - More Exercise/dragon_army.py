from collections import defaultdict

dragons = defaultdict(dict)
default_values = (45, 250, 10)
dragon_stats = ("damage", "health", "armour")

for _ in range(int(input())):
    colour, name, damage, health, armour = input().split()

    # each variable is converted to int if it is not null by using the
    # index from enumerate as an index in the default values tuple
    damage, health, armour = [
        int(variable) if variable != "null" else default_values[index]
        for index, variable in enumerate((damage, health, armour))
    ]

    # {"Colour": {"Dragon Name": {"damage": 25, "health": 250, "armour": 10}}}
    dragons[colour][name] = {"damage": damage, "health": health, "armour": armour}

for colour, members in dragons.items():
    # the key is the stat, the value is the sum of each dragon's value for that stat,
    # divided by the total number of dragons to get the average
    average = {
        stat: sum(dragon[stat] / len(members) for dragon in members.values())
        for stat in dragon_stats
    }

    print(
        f"{colour}::({average['damage']:.2f}/"
        f"{average['health']:.2f}/"
        f"{average['armour']:.2f})"
    )

    # print the all the dragons that are the current colour, sorted alphabetically
    for dragon_name, stats in sorted(members.items(), key=lambda name: name[0]):
        damage, health, armour = stats.values()
        print(f"-{dragon_name} -> damage: {damage}, health: {health}, armor: {armour}")
