lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

expenses += (lost_fights_count // 2) * helmet_price
expenses += (lost_fights_count // 3) * sword_price
expenses += (lost_fights_count // 6) * shield_price
expenses += (lost_fights_count // 12) * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")