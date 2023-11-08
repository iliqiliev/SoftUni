elements = [element.lower() for element in input().split()]
occurrences = {}

for element in elements:
    if element not in occurrences:
        occurrences[element] = 0

    occurrences[element] += 1

for element, appearances in occurrences.items():
    if appearances & 1:
        print(element, end=" ")
