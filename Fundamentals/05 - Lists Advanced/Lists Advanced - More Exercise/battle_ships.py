def main():

    field_size = int(input())
    field = []

    for _ in range(field_size):
        field.append([int(number) for number in input().split()])

    instructions = [(int(index[0]), int(index[2]))
                    for index in input().split()]

    print(ship_combat(field, instructions))


def ship_combat(field: list, instructions: list) -> int:

    sank = 0
    for instruction in instructions:

        if field[instruction[0]][instruction[1]] == 1:
            sank += 1
        field[instruction[0]][instruction[1]] -= 1

    return sank


if __name__ == "__main__":
    main()
