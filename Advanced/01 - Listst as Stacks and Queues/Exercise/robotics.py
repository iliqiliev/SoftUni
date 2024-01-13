from collections import deque
from datetime import datetime, timedelta


robots = {name: [int(process_time), 0]
          for robot_info in input().split(";")
          for name, process_time in [robot_info.split("-")]}


time = datetime.strptime(input(), "%H:%M:%S")
# callable is called until it returns the sentinel  
items_queue = deque(product for product in iter(input, "End"))

while items_queue:
    time += timedelta(seconds=1)

    for name, robot_info in robots.items():
        if robot_info[1] > 0:
            robots[name][1] -= 1

    free_robot = next((robot for robot in robots.items() if robot[1][1] == 0), None)

    if not free_robot:
        items_queue.rotate(-1)
        continue

    robot_name = free_robot[0]
    print(f"{robot_name} - {items_queue.popleft()} [{time.time()}]")
    robots[robot_name][1] = robots[robot_name][0]
