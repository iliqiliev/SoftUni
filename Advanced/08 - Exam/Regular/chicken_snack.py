from collections import deque


pocket_money = list(map(int, input().split()))
food_prices = deque(map(int, input().split()))

gluttony_level = 4
food_eaten = 0

while pocket_money and food_prices:
    current_money = pocket_money.pop()
    current_price = food_prices.popleft()

    if current_money < current_price:
        continue

    if current_money > current_price:
        if pocket_money:
            change = current_money - current_price
            pocket_money[-1] += change

    food_eaten += 1

if not food_eaten:
    print("Henry remained hungry. He will try next weekend again.")

else:

    if food_eaten >= gluttony_level:
        print("Gluttony of the day!", end=" ")

    plural_form = 's' * (food_eaten > 1)
    misc_softuni_character = ':' * (food_eaten < gluttony_level)  # wtf

    print(
        f"Henry ate{misc_softuni_character} {food_eaten} food{plural_form}."
    )
