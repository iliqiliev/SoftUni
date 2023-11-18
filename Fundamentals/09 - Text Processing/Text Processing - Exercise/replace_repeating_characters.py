string = input()
string_no_repeats = ""

last_character = ""
for character in string:
    if character != last_character:
        string_no_repeats += character
        last_character = character

print(string_no_repeats)
