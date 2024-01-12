from collections import deque


dispenser_queue = deque()
water = int(input())

while True:
    name = input()
    if name == "Start":
        break

    dispenser_queue.append(name)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{water} liters left")
        break

    if len(command) == 1:
        required_water = int(command[0])
        if required_water <= water:
            print(f"{dispenser_queue.popleft()} got water")
            water -= required_water

        else:
            print(f"{dispenser_queue.popleft()} must wait")

    else:
        refill = int(command[1])
        water += refill
