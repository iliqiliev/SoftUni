from collections import deque

queue = deque()


while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break

    if command == "Paid":
        while queue:
            print(queue.popleft())

        continue

    queue.append(command)  # name
