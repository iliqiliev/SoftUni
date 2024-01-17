sets_lengths = tuple(int(length) for length in input().split())

first_set = {input() for _ in range(sets_lengths[0])}
second_set = {input() for _ in range(sets_lengths[1])}

print("\n".join(first_set & second_set))  # intersection
