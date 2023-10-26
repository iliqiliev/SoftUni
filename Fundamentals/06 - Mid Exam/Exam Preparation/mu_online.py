def main(max_health=100, bitcoin=0):

    dungeon_layout = [room.split() for room in input().split("|")]
    health = max_health
    room_counter = 0

    for room in dungeon_layout:
        encounter, value = room[0], int(room[1])
        room_counter += 1

        if encounter == "potion":
            health += heal(health, max_health, value)

        elif encounter == "chest":
            bitcoin += value
            print(f"You found {value} bitcoins.")

        else:
            health = fight_monster(health, encounter, value, room_counter)
            if health <= 0:
                # if you've not managed to fight the monster
                break

    else:
        print(f"You've made it!\n"
              f"Bitcoins: {bitcoin}\n"
              f"Health: {health}")


def heal(health: int, max_health: int, potion: int) -> int:
    # avoid over-healing
    heal = min(potion, max_health - health)
    health += heal

    print(f"You healed for {heal} hp.\n"
          f"Current health: {health} hp.")

    return heal


def fight_monster(health: int, monster: str, monster_attack: int, room_counter: int) -> int:
    health -= monster_attack

    if health > 0:
        print(f"You slayed {monster}.")

    else:
        print(f"You died! Killed by {monster}.\n"
              f"Best room: {room_counter}")

    return health


if __name__ == "__main__":
    main()
