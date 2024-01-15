import sys
from collections import deque


green_duration = int(input())
yellow_duration = int(input())
car_queue = deque()
car_counter = 0

command = input()
while command != "END":
    if command == "green":
        green_left = green_duration

        while green_left > 0 and car_queue:
            car = car_queue.popleft()
            time_left = green_left + yellow_duration

            if time_left >= len(car):
                car_counter += 1
                green_left -= len(car)

            else:
                print(f"A crash happened!\n{car} was hit at {car[time_left]}.")
                sys.exit(1)  # where is break 2

    else:
        car_queue.append(command)

    command = input()

print(f"Everyone is safe.\n{car_counter} total cars passed the crossroads.")
