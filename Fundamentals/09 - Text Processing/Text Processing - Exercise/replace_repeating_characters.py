string = input()
string_no_repeats = ""

for next_index, character in enumerate(string[:-1], 1):
    next_character = string[next_index]
    
    if character != next_character:
        string_no_repeats += character

# add the last character because the loop would miss it
if string:    
    string_no_repeats += string[-1]

print(string_no_repeats)
