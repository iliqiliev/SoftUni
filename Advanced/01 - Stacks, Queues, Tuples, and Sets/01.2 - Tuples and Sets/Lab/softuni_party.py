guests = {input() for _ in range(int(input()))}
visitors = set(iter(input, "END"))

remaining_guests = guests - visitors

print(len(remaining_guests))
print("\n".join(sorted(remaining_guests)))
