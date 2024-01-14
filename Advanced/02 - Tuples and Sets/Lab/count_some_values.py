values = tuple(float(value) for value in input().split())
counted_values = set()

for value in values:
    if value not in counted_values:
        print(f"{value} - {values.count(value)} times")

    counted_values.add(value)
