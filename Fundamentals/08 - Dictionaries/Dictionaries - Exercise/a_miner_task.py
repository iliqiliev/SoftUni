from collections import defaultdict


mined_resources = defaultdict(int)
while True:  # can't use walrus, old python version
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    mined_resources[resource] += quantity

for resource, quantity in mined_resources.items():
    print(f"{resource} -> {quantity}")
