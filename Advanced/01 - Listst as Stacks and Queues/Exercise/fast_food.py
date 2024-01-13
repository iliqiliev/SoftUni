from collections import deque


food_quantity = int(input())
orders = deque(int(order) for order in input().split())

print(max(orders))
for _ in range(len(orders)):
    if orders[0] <= food_quantity:
        food_quantity -= orders[0]
        orders.popleft()

    else:
        print("Orders left:", *orders)
        break

else:
    print("Orders complete")
