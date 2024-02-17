string = input()
digits = ""
letters = ""
other = ""

for character in string:
    if character.isalpha():
        letters += character

    elif character.isdigit():
        digits += character
    else:
        other += character

print(digits)
print(letters)
print(other)
