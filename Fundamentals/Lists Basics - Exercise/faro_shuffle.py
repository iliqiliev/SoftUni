list_of_strings = input().split()
middle = len(list_of_strings) // 2
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    first_half = list_of_strings[:middle]
    second_half = list_of_strings[middle:]
    
    for index in range(len(list_of_strings)):
        if not index % 2: # if even
            list_of_strings[index] = first_half[index // 2]
        else:
            list_of_strings[index] = second_half[index // 2]

print(list_of_strings)