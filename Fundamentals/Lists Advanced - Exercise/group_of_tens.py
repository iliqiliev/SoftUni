import math


numbers = [int(number) for number in input().split(", ")]
groups = range(1, math.ceil(max(numbers) / 10) + 1)

for group in groups:

    group_numbers = [number for number in numbers if number <= (group * 10)]
    numbers = [number for number in numbers if number not in group_numbers]

    print(f"Group of {group * 10}'s: {group_numbers}")
