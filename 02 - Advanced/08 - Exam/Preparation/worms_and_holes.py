from collections import deque
from typing import Deque, List, Union


def format_sequence(label: str, sequence: Union[List[int], Deque[int]]) -> str:
    return f"{label} left: {', '.join(map(str, sequence)) or 'none'}"


worms = [int(worm) for worm in input().split()]
holes = deque(int(hole) for hole in input().split())

matches = 0
initial_worms_count = len(worms)

while worms and holes:
    current_worm = worms.pop()

    if current_worm <= 0:
        continue

    current_hole = holes.popleft()

    if current_worm != current_hole:
        worms.append(current_worm - 3)
        continue

    matches += 1


print(f"Matches: {matches}" if matches else "There are no matches.")

if matches == initial_worms_count:
    print("Every worm found a suitable hole!")

else:
    print(format_sequence("Worms", worms))

print(format_sequence("Holes", holes))
