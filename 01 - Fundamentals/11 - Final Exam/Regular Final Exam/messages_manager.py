def message_add(users: dict, username: str, sent: int, received: int) -> dict:
    if username not in users:
        users[username] = {"sent": sent, "received": received}

    return users


def message_send(users: dict, max_messages: int, sender: str, receiver: str) -> dict:
    def check_capacity(users: dict, max_messages: int, username: str) -> dict:
        if sum(users[username].values()) >= max_messages:
            users.pop(username)
            print(f"{username} reached the capacity!")

        return users

    if sender in users and receiver in users:

        users[sender]["sent"] += 1
        check_capacity(users, max_messages, sender)

        users[receiver]["received"] += 1
        check_capacity(users, max_messages, receiver)

    return users


def message_empty(users: dict, username: str) -> dict:
    if username == "All":
        users.clear()

    else:
        users.pop(username, None)

    return users


def main():
    max_messages = int(input())
    users = {}

    commands = {
        "Add": message_add,
        "Message": message_send,
        "Empty": message_empty,
    }

    while True:
        command, *arguments = input().split("=")
        if command not in commands:
            break

        arguments = [int(arg) if arg.isdigit() else arg for arg in arguments]

        if command == "Message":  # to avoid passing max_messages to every function
            users = commands[command](users, max_messages, *arguments)

        else:
            users = commands[command](users, *arguments)

    print(f"Users count: {len(users)}")
    for username, user_stats in users.items():
        print(f"{username} - {sum(user_stats.values())}")


if __name__ == "__main__":
    main()
