def pass_make(password: str, case: str, index: int) -> str:
    case_function = str.upper if case == "Upper" else str.lower
    return password[:index] + case_function(password[index]) + password[index + 1:]


def pass_insert(password: str, index: int, char: str) -> str:
    if index in range(len(password)):
        password = password[:index] + char + password[index:]

    return password


def pass_replace(password: str, char: str, value: int) -> str:
    new_char = chr(ord(char) + value)
    return password.replace(char, new_char)


def pass_validate(password: str) -> None:
    if len(password) < 8:
        print("Password must be at least 8 characters long!")

    if not password.replace("_", "").isalnum():
        print("Password must consist only of letters, digits and _!")

    if not any(char.isupper() for char in password):
        print("Password must consist at least one uppercase letter!")

    if not any(char.islower() for char in password):
        print("Password must consist at least one lowercase letter!")

    if not any(char.isdigit() for char in password):
        print("Password must consist at least one digit!")


def main():
    password = input()

    while True:
        command, *arguments = input().split()
        if command == "Complete":
            break

        if command == "Make":
            password = pass_make(password, arguments[0], int(arguments[1]))
            print(password)

        elif command == "Insert":
            password = pass_insert(password, int(arguments[0]), arguments[1])
            print(password)

        elif command == "Replace":
            password = pass_replace(password, arguments[0], int(arguments[1]))
            print(password)

        elif command == "Validation":
            pass_validate(password)


if __name__ == "__main__":
    main()
