# print([round(float(num)) for num in input().split()])

rounding = lambda numbers: [round(num) for num in numbers]

unrounded_numbers = [float(num) for num in input().split()]
rounded_numbers = rounding(unrounded_numbers)

print(rounded_numbers)
