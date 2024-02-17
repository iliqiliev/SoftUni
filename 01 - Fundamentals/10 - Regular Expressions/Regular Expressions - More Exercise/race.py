import re
from collections import defaultdict


valid_racers = input().split(", ")
racers = defaultdict(int)

while True:
    command = input()
    if command == "end of race":
        break

    name = "".join(re.findall(r"[A-Za-z]+", command))
    distance = sum(int(digit) for digit in re.findall(r"\d", command))

    if name in valid_racers:
        racers[name] += distance

podium = tuple(
    item[0] for item in sorted(racers.items(), key=lambda distance: -distance[1])[:3]
)
print(f"1st place: {podium[0]}")
print(f"2nd place: {podium[1]}")
print(f"3rd place: {podium[2]}")
