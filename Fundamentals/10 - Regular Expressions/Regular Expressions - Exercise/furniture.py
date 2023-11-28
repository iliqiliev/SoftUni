import re


purchase_information_pattern = r"""
    >>(?P<item>[A-Za-z\s]+)
    <<(?P<price>(?:[0]|[1-9][\d]*)(?:\.?\d+)?)
    !(?P<quantity>\d+)
    """
bought_furniture = []
total_price = 0

while True:
    command = input()
    if command == "Purchase":
        break

    purchase = re.match(purchase_information_pattern, command, re.VERBOSE)
    if purchase:
        item = purchase["item"]
        total_item_price = float(purchase["price"]) * int(purchase["quantity"])

        bought_furniture.append(item)
        total_price += total_item_price

print("Bought furniture:")
for name in bought_furniture:
    print(name)
print(f"Total money spend: {total_price:.2f}")
