import operator
from collections import deque


operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

bees = deque(int(num) for num in input().split())
nectars = [int(num) for num in input().split()]
process = deque(input().split())

honey = 0

while bees and nectars:
    current_bee = bees[0]
    current_nectar = nectars.pop()

    if current_nectar >= current_bee:
        bees.popleft()  # the bee is not removed if the nectar is less than it
        current_operation = process.popleft()

        if current_operation == "/" and current_nectar < 1:
            continue

        honey += abs(operators[current_operation](current_bee, current_nectar))

print(f"Total honey made: {honey}")
if bees:
    print("Bees left:", ", ".join(str(bee) for bee in bees))

if nectars:
    print("Nectar left:", ", ".join(str(nectar) for nectar in nectars))
