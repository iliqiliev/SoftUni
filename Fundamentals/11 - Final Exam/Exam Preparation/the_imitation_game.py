def move(message: str, number_of_letters: int) -> str:
    number_of_letters = int(number_of_letters)
    return message[number_of_letters:] + message[:number_of_letters]


def insert(message: str, index: int, value: str) -> str:
    index = int(index)
    return message[:index] + value + message[index:]


def change_all(message: str, substring: str, replacement: str) -> str:
    return message.replace(substring, replacement)


def main():
    message = input()

    # if this is obtuse imagine lambda functions inside the dictionary :D
    operations = {
        "Move": move,
        "Insert": insert,
        "ChangeAll": change_all,
    }

    while True:
        command, *arguments = input().split("|")
        if command not in operations:
            print(f"The decrypted message is: {message}")
            break

        message = operations[command](message, *arguments)


if __name__ == "__main__":
    main()
