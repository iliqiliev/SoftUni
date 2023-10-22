def main():

    phones = input().split(", ")

    command = input().split(" - ")
    while command[0] != "End":
        option = command[0]
        phone = (command[1]).partition(":")[0]

        if phone in phones:
            if option == "Remove":
                remove_phone(phones, phone)

            elif option == "Bonus phone":
                new_phone = (command[1]).split(":")[1]
                bonus_phone(phones, phone, new_phone)

            elif option == "Last":
                last_phone(phones, phone)

        else:
            if option == "Add":
                add_phone(phones, phone)

        command = input().split(" - ")

    print(", ".join(phones))


def remove_phone(phones: list, phone: str) -> None:
    phones.remove(phone)


def bonus_phone(phones: list, old_phone: str, new_phone: str) -> None:
    new_phone_index = phones.index(old_phone) + 1
    phones.insert(new_phone_index, new_phone)


def last_phone(phones: list, phone: str) -> None:
    phones.remove(phone)
    phones.append(phone)


def add_phone(phones: list, phone: str) -> None:
    phones.append(phone)


if __name__ == "__main__":
    main()
