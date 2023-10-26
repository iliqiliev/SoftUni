numbers = input().split()
string = [*input()]
message = []

for number in numbers:
    sum_of_current_number = sum([int(x) for x in number])
    current_string_length = len(string)
    current_char = string[sum_of_current_number % current_string_length]
    message.append(current_char)
    string.remove(current_char)
    print(current_char, end="")