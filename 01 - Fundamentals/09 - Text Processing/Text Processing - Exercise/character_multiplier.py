from itertools import zip_longest


first_word, second_word = input().split()
total_sum = 0

# if one of the words is shorter its character is replaced by chr(1)
# this way the math checks out
for first_char, second_char in zip_longest(first_word, second_word, fillvalue=chr(1)):
    total_sum += ord(first_char) * ord(second_char)

print(total_sum)
