characters = input().split(", ")
ascii_dict = {}

for character in characters:
    ascii_dict[character] = ord(character)
    
print(ascii_dict)