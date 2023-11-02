starting_char = int(input())
ending_char = int(input())

for ascii_index in range(starting_char, ending_char + 1):
    print(chr(ascii_index), end=" ")
