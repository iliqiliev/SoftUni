import re

longest_intersection = set()
ranges_regex = re.compile(r"(\d+),(\d+)-(\d+),(\d+)")

for _ in range(int(input())):
    current = ranges_regex.match(input())
    if not current:  # appeasing the IDE
        continue

    current = tuple(int(num) for num in current.groups())

    first_range = set(range(current[0], current[1] + 1))
    second_range = set(range(current[2], current[3] + 1))
    current_intersection = first_range & second_range

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

formatted_intersection = ", ".join(f"{num}" for num in longest_intersection)
print(f"Longest intersection is [{formatted_intersection}]",
      f"with length {len(longest_intersection)}")
