import re


valid_message_pattern = re.compile(
    r"""(?x)
    !(?P<command>[A-Z][a-z]{2,})!:
    \[(?P<string>[A-Za-z]{8,})\]
"""
)

for _ in range(int(input())):
    valid_message = valid_message_pattern.fullmatch(input())

    if valid_message:
        command = valid_message.group('command')
        numbers = " ".join(str(ord(char)) for char in valid_message.group('string'))
        print(f"{command}: {numbers}")

    else:
        print("The message is invalid")
