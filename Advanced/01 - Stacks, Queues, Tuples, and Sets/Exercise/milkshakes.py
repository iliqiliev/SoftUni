from collections import deque


chocolates = [int(num) for num in input().split(", ")]
milk_cups = deque(int(num) for num in input().split(", "))

milkshake_count = 0

while milkshake_count < 5 and chocolates and milk_cups:

    current_chocolate = chocolates[-1]
    current_milk = milk_cups[0]

    if current_chocolate < 1 or current_milk < 1:
        if current_chocolate < 1:
            chocolates.pop()

        if current_milk < 1:
            milk_cups.popleft()

        continue

    if current_chocolate == current_milk:
        milkshake_count += 1
        chocolates.pop()
        milk_cups.popleft()

    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5


chocolates_formatted = (", ".join(str(value)
                                  for value in chocolates)) if chocolates else "empty"
milk_cups_formatted = (", ".join(str(value)
                                 for value in milk_cups)) if milk_cups else "empty"

if milkshake_count >= 5:
    print("Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

print(f"Chocolate: {chocolates_formatted}")
print(f"Milk: {milk_cups_formatted}")
