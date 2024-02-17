text = input()

for character in sorted(set(text)):
    print(f"{character}: {text.count(character)} time/s")
