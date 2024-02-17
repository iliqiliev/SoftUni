import re


food_info_pattern = r"""
    (?P<sep>[#|])
    (?P<item_name>[A-Za-z\s]+)
    (?P=sep)
    (?P<exp_date>\d{2}/\d{2}/\d{2})
    (?P=sep)
    (?P<calories>\d{1,4})
    (?P=sep)
    """

food_storage = [
    {
        "name": item[1],
        "exp_date": item[2],
        "calories": int(item[3]),
    }
    for item in re.findall(food_info_pattern, input(), re.VERBOSE)
]

daily_calories = 2000
total_calories = sum(item["calories"] for item in food_storage)

print(f"You have food to last you for: {total_calories // daily_calories} days!")
for item in food_storage:
    print(f"Item: {item['name']}, Best before: {item['exp_date']}, "
          f"Nutrition: {item['calories']}")
