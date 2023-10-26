list_of_strings = input().split()
middle = len(list_of_strings) // 2
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    first_half = list_of_strings[:middle]
    second_half = list_of_strings[middle:]
    list_of_strings = []
    
    for index in range(middle):
        list_of_strings.append(first_half[index])
        list_of_strings.append(second_half[index])

print(list_of_strings)