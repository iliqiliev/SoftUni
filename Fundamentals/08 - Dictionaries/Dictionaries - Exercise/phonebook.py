phonebook = {}

while True:
    entry = input().split("-")

    if len(entry) == 1:
        break

    #         name        number
    phonebook[entry[0]] = entry[1]

for search in range(int(*entry)):
    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")

    else:
        print(f"Contact {name} does not exist.")
