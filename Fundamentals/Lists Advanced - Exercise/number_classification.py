numbers = input().split(", ")

positive = ", ".join([number for number in numbers if int(number) >= 0])
negative = ", ".join([number for number in numbers if int(number) < 0])
even = ", ".join([number for number in numbers if not (int(number) & 1)])
odd = ", ".join([number for number in numbers if (int(number) & 1)])

print(f"Positive: {positive}\n"
      f"Negative: {negative}\n"
      f"Even: {even}\n"
      f"Odd: {odd}")