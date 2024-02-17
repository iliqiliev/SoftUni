message = input()

operations = {
    "Move": lambda message, number_of_letters:
    message[number_of_letters:] + message[:number_of_letters],

    "Insert": lambda message, index, value:
    message[:index] + value + message[index:],

    "ChangeAll": lambda message, substring, replacement:
    message.replace(substring, replacement),
}

while True:
    command, *arguments = input().split("|")
    if command not in operations:
        print(f"The decrypted message is: {message}")
        break

    arguments = [int(arg) if arg.isdigit() else arg for arg in arguments]
    message = operations[command](message, *arguments)
