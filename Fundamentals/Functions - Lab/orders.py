def total_price(product: str, quantity: int) -> float:
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1.00
    elif product == "snacks":
        return quantity * 2.00
    else:
        return 0
    
      
product = input()
quantity = int(input())

order = total_price(product, quantity)
print(f"{order:.2f}")