elements = input().split()
moves = 0

command = input()
while command != "end":
    # i
    moves += 1

    a, b = map(int, command.split())
    # equal indices or either index not valid
    cheat = a == b or not (0 <= a < len(elements) and 0 <= b < len(elements))

    if cheat:
        mid = len(elements) // 2
        elements = elements[:mid] + \
            [f"-{moves}a", f"-{moves}a"] + elements[mid:]
        print("Invalid input! Adding additional elements to the board")

    else:  # not cheated
        a_value, b_value = elements[a], elements[b]
        if a_value == b_value:
            print(f"Congrats! You have found matching elements - {a_value}!")
            elements = [el for el in elements if el != a_value]

            if not elements:
                print(f"You have won in {moves} turns!")
                break

        else:  # not a pair
            print("Try again!")

    command = input()

else:
    # are there any elements left?
    if elements:
        print("Sorry you lose :(")
        print(*elements)
    else:  # no - you've won
        print(f"You have won in {moves} turns!")
