numbers = [int(x) for x in input().split(", ")]

positive = ", ".join([str(number) for number in numbers if number >= 0])
negative = ", ".join([str(number) for number in numbers if number < 0])
even = ", ".join([str(number) for number in numbers if not (number & 1)])
odd = ", ".join([str(number) for number in numbers if (number & 1)])

print(f"Positive: {positive}\n"
      f"Negative: {negative}\n"
      f"Even: {even}\n"
      f"Odd: {odd}")