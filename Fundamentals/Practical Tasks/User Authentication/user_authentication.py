import os
import sys
import getpass
import random
from enum import Enum
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Command(Enum):
    LOGIN = 1
    REGISTER = 2
    EXIT = 0


def clear_screen() -> None:
    # Linux or macOS
    if os.name == "posix":
        os.system("clear")
    # Winblows
    else:
        os.system("cls")


def login(credentials: dict) -> str | None:
    username = input("Enter your username: ").strip()
    password = bytes(getpass.getpass("Enter your password: ").strip(), "utf-8")

    if username not in credentials:
        print(f"{username} is not registered.")
        return None

    try:
        PasswordHasher().verify(credentials[username]["hashed_password"], password)
        print(f"Successfully logged into {username}")

        # update hash if argon2 parameters have changed (more secure)
        if PasswordHasher().check_needs_rehash(
            credentials[username]["hashed_password"]
        ):
            credentials[username]["hashed_password"] = PasswordHasher().hash(password)

        return username

    except VerifyMismatchError:
        print("Provided password is incorrect.")
        return None


def user_profile(user: str, credentials: dict[str, dict[str, str]]) -> None:
    clear_screen()

    print(f"Hello, {user},\n")
    input("Welcome to your dashboard. Press Enter to see your details. ")

    for detail, content in credentials[user].items():
        # don't show the hashed password
        if detail == "hashed_password":
            continue

        print(f"{detail.replace('_', ' ').title()} - {content}")


def valid_credentials(name: str, password: bytes, credentials: dict) -> str | None:
    # usernames must be at least 4 characters long and passwords - 8
    # usernames must also be unique
    if name in credentials:
        return f"{name} already exists."

    if len(name) < 4:
        return "Username must be 4 characters or longer."

    if len(password) < 8:
        return "Password must be 8 characters or longer."

    return None


def register(credentials: dict) -> bool:
    username = input("Enter username: ").strip()
    password = bytes(getpass.getpass("Enter password: ").strip(), "utf-8")

    error = valid_credentials(username, password, credentials)
    if error:
        print(error)
        return False

    credentials[username] = {
        "hashed_password": PasswordHasher().hash(password),
        "full_name": f"{username.capitalize()} {username.capitalize()}ev",
        "email": f"{username}{random.randint(100, 1000)}@gmail.com",
        "phone_number": f"08{random.randint(7,10)}{random.randint(1000000, 10000000)}",
    }
    print(f"Success! {username} is now registered.")
    return True


def main():
    user_credentials = {}

    while True:
        clear_screen()

        print("1. Login")
        print("2. Register")
        print("0. Exit")

        try:
            command = Command(int(input("Press a key to select an option [1/2/0]: ")))

        except ValueError:
            input("Invalid option! Press Enter to continue.")
            continue

        match command:
            case Command.LOGIN:
                logged_name = login(user_credentials)
                if logged_name:
                    user_profile(logged_name, user_credentials)

            case Command.REGISTER:
                register(user_credentials)

            case Command.EXIT:
                sys.exit()

        input("Press Enter to continue.")


if __name__ == "__main__":
    main()
