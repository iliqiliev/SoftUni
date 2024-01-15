from collections import deque


cups = deque(int(cup) for cup in input().split())
bottles = [int(bottle) for bottle in input().split()]
wasted_water = 0

while cups and bottles:
    cup_current = cups[0]
    bottle_current = bottles.pop()

    if bottle_current >= cup_current:  # the cup is filled/overfilled
        wasted_water += (bottle_current - cups.popleft())

    else:  # the cup remains partly filled
        cups[0] -= bottle_current

if bottles:
    print("Bottles:", *bottles)

else:
    print("Cups:", *cups)

print(f"Wasted litters of water: {wasted_water}")
