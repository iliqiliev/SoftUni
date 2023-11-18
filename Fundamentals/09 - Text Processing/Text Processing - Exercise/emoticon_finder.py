text = input()

# avoids an IndexError if the last character is ":"
for next_index, character in enumerate(text[:-1], 1):
    if character == ":":
        print(f"{character}{text[next_index]}")
