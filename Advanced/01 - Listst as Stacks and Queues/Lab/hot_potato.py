from collections import deque


children = deque(input().split())
eliminating_toss = int(input())

while len(children) > 1:
    children.rotate(-(eliminating_toss - 1))  # anticlockwise
    print(f"Removed {children.popleft()}")

print(f"Last is {children[0]}")
