items_list = [item.split('->') for item in input().split('|')]
available_money = int(input())
potential_profit = 0
profit = 0

item_prices = {
    'Clothes': 50.0,
    'Shoes': 35.0,
    'Accessories': 20.5,
}

for item in items_list:
    item_type, item_price = item[0], float(item[1])
    
    if item_type in item_prices and \
       item_price <= item_prices[item_type] and \
       available_money >= item_price:
        available_money -= item_price
        potential_profit += item_price * 1.4
        profit += item_price * 0.4
        
        print(f"{item_price * 1.4:.2f}", end=" ")
        if available_money + potential_profit >= 150:
            break
    
print(f"\nProfit: {profit:.2f}")
if available_money + potential_profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")