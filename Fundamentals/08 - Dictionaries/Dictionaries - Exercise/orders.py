orders = {}

while True:
    order = input().split()
    if order[0] == "buy":
        break

    product, price, quantity = order[0], float(order[1]), int(order[2])
    orders.setdefault(product, {"price": 0, "quantity": 0})

    orders[product]["price"] = price
    orders[product]["quantity"] += quantity

for product, details in orders.items():
    total_price = details["price"] * details["quantity"]
    print(f"{product} -> {total_price:.2f}")
