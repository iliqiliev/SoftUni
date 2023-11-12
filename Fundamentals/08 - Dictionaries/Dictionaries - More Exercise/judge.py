from collections import defaultdict


entries = defaultdict(dict)

while True:
    command = input().split(" -> ")
    if len(command) != 3:
        break

    name, contest, points = command
    points = int(points)

    entries[contest][name] = max(points, entries[contest].get(name, 0))


for contest, participants in entries.items():
    print(f"{contest}: {len(participants)} participants")

    # sort the participants by the biggest score (-x[1])
    # and then by name alphabetically (x[0])
    ranked = enumerate(sorted(participants.items(), key=lambda x: (-x[1], x[0])), 1)
    for index, (participant, score) in ranked:
        print(f"{index}. {participant} <::> {score}")

individual_standings = defaultdict(int)
for participants in entries.values():
    for participant, score in participants.items():
        individual_standings[participant] += score

print("Individual standings:")
# The second part of the sorting key fixes 66/100 on Judge, was a pain to find because:
# "If all sorting criteria fail, the order should be by order of input." (: (:
ranked = enumerate(sorted(individual_standings.items(), key=lambda x: (-x[1], x)), 1)
for index, (participant, score) in ranked:
    print(f"{index}. {participant} -> {score}")
