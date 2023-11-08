products = {}

command = input()
while command != "statistics":
    product, count = command.split(": ")

    if product not in products:
        products[product] = 0

    products[product] += int(count)

    command = input()
    
print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}\n"
      f"Total Quantity: {sum(products.values())}")