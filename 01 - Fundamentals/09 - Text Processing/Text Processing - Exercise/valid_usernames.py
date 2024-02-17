def valid_username(name: str) -> bool:
    if (
        all(char.isalnum() or char in ("_", "-") for char in name)
        and 3 <= len(name) <= 16
    ):
        return True

    return False


usernames = input().split(", ")

for username in usernames:
    if valid_username(username):
        print(username)
