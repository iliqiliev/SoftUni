shopping_list = input().split("!")

command = input()
while command != "Go Shopping!":

    command, item, *new_item = command.split()
    if new_item:
        new_item = new_item[0]

    if item in shopping_list:
        if command == "Unnecessary":
            shopping_list.remove(item)

        elif command == "Correct":
            index = shopping_list.index(item)
            shopping_list[index] = new_item  # type: ignore (vscode)

        elif command == "Rearrange":
            shopping_list.remove(item)
            shopping_list.append(item)

    else:
        if command == "Urgent":
            shopping_list.insert(0, item)

    command = input()

print(*shopping_list, sep=", ")
