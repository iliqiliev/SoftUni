from collections import defaultdict


occurrences = defaultdict(int)
string = input().replace(" ", "")

for character in string:
    occurrences[character] += 1

for character, appearances in occurrences.items():
    print(f"{character} -> {appearances}")
