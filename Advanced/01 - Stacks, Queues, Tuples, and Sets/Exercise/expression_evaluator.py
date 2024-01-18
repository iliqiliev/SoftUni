import operator
from collections import deque


expression = [num if num in ("*", "+", "-", "/") else int(num)
              for num in input().split()]

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

queue = deque()
for current in expression:
    if isinstance(current, int):
        queue.append(current)

    else:
        for _ in range(len(queue) - 1):
            # for example operator.add(1, 2) -> 3
            queue[0] = operators[current](queue.popleft(), queue[0])

print(*queue)
