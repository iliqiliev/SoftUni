from collections import deque


petrol_stations = int(input())
# fuel as positive and distance as negative; (input().split(),) to make it a tuple
journey_info = deque((int(x), -int(y)) for _ in range(petrol_stations)
                     for x, y in (input().split(),))

for fuel_pump in range(petrol_stations):
    fuel = 0
    for station in journey_info:
        fuel += sum(station)

        if fuel < 0:
            journey_info.rotate(-1)  # onto the next station
            break

    else:  # this loop completed so the journey is possible
        print(fuel_pump)
        break
