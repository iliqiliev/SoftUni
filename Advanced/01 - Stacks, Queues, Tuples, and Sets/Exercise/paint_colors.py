from collections import deque


colours = {"red", "yellow", "blue", "orange", "purple", "green"}
colours_bases = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
colours_found = []
substrings = deque(input().split())

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else str()

    for combination in left + right, right + left:
        if combination in colours:
            colours_found.append(combination)
            break

    else:
        for part in left, right:
            if part[:-1]:
                substrings.insert((len(substrings) // 2), part[:-1])

for colour in set(colours_bases).intersection(colours_found):
    if not colours_bases[colour].issubset(colours_found):
        colours_found.remove(colour)

print(colours_found)
