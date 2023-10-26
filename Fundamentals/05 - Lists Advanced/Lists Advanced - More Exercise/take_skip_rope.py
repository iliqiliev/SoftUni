input_string = input()
numbers_list = [int(char) for char in input_string if char.isdigit()]
string = "".join([char for char in input_string if not char.isdigit()])

result_string = ""

counter = 0
for index, number in enumerate(numbers_list):
    # always add to the counter but only
    # add to the string when the index is even
    if not (index & 1):
        result_string += string[counter: counter + number]

    counter += number

print(result_string)
