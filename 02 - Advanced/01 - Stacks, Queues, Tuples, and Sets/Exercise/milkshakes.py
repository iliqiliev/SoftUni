from collections import deque


chocolates = [int(num) for num in input().split(", ")]
milk_cups = deque(int(num) for num in input().split(", "))

milkshake_count = 0

while chocolates and milk_cups:

    current_chocolate = chocolates.pop()
    current_milk = milk_cups.popleft()

    if current_chocolate < 1 or current_milk < 1:
        if current_chocolate > 0:
            chocolates.append(current_chocolate)

        if current_milk > 0:
            milk_cups.appendleft(current_milk)

        continue

    if current_chocolate == current_milk:
        milkshake_count += 1
        if milkshake_count == 5:
            print("Great! You made all the chocolate milkshakes needed!")
            break

    else:
        milk_cups.append(current_milk)
        chocolates.append(current_chocolate - 5)

else:
    print("Not enough milkshakes.")

chocolates_formatted = (", ".join(str(value) for value in chocolates)) or "empty"
print(f"Chocolate: {chocolates_formatted}")

milk_cups_formatted = (", ".join(str(value) for value in milk_cups)) or "empty"
print(f"Milk: {milk_cups_formatted}")
