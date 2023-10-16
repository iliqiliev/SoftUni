number = int(input())
number_binary = bin(number)[2:] # ignore first two chars (0b), they indicate binary number
binary_digit = input()

count = number_binary.count(binary_digit)

print(count)