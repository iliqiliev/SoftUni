import re

order_pattern = r"""
    %(?P<name>[A-Z][a-z]*)%.*?
    <(?P<product>\w+)>.*?
    \|(?P<quantity>\d+)\|.*?
    (?P<price>\d+(?:\.\d+)?)\$
    """

total_income = 0
while True:
    command = input()
    if command == "end of shift":
        break

    valid_order = re.match(order_pattern, command, re.VERBOSE)
    if valid_order:
        order_price = int(valid_order["quantity"]) * float(valid_order["price"])
        total_income += order_price

        print(f"{valid_order['name']}: {valid_order['product']} - {order_price:.2f}")

print(f"Total income: {total_income:.2f}")
