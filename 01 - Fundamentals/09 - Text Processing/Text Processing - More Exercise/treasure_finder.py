key = [int(number) for number in input().split()]

while True:
    encrypted_message = input()
    if encrypted_message == "find":
        break

    decrypted_message = ""
    for index, character in enumerate(encrypted_message):
        key_index = index % len(key)

        decrypted_message += chr(ord(character) - key[key_index])

    material = decrypted_message.split("&")[1]
    coordinates = decrypted_message[decrypted_message.index("<") + 1 : -1]

    print(f"Found {material} at {coordinates}")
