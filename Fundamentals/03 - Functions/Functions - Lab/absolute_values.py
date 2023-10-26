absolute_values = lambda x: [abs(value) for value in x]

input_list = [float(x) for x in input().split()]

print(absolute_values(input_list))