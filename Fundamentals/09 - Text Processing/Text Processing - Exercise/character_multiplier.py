first_word, second_word = input().split()
total_sum = 0

for first_char, second_char in zip(first_word, second_word):
    total_sum += ord(first_char) * ord(second_char)

# if one of the words is longer add the unicode code for every character
# that it is longer than the other word to the total sum
if len(first_word) > len(second_word):
    total_sum += sum(ord(char) for char in first_word[len(second_word) :])

elif len(second_word) > len(first_word):
    total_sum += sum(ord(char) for char in second_word[len(first_word) :])

print(total_sum)
