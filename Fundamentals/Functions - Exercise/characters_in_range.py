def ascii_range(a: str, b: str) -> str:
    
    chars = str()
    
    for char in range(ord(a) + 1, ord(b)):
        chars += chr(char) + " "
        
    return chars.rstrip()


starting_character = input()
ending_character = input()

print(ascii_range(starting_character, ending_character))