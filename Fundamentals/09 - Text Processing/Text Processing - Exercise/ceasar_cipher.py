plain_text = input()

encrypted_text = "".join([chr(ord(char) + 3) for char in plain_text])

print(encrypted_text)
