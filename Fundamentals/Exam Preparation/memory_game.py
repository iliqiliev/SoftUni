elements = input().split()
moves = 0

command = input().split()
while command[0] != "end":
    moves += 1

    a, b = int(command[0]), int(command[1])

    cheat = a == b or not (0 <= a < len(elements) and 0 <= b < len(elements))

    if cheat:
        mid = len(elements) // 2
        elements = elements[:mid] + \
            [f"-{moves}a", f"-{moves}a"] + elements[mid:]
        print("Invalid input! Adding additional elements to the board")

    else:
        a_value, b_value = elements[a], elements[b]
        if a_value == b_value:
            print(f"Congrats! You have found matching elements - {a_value}!")
            elements = [el for el in elements if el != a_value]
            if not elements:
                print(f"You have won in {moves} turns!")
                break

        else:
            print("Try again!")

    command = input().split()

else:
    if elements:
        print("Sorry you lose :(")
        print(*elements)
    else:
        print(f"You have won in {moves} turns!")
