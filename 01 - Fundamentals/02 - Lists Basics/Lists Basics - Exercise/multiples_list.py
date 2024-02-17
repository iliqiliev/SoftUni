factor = int(input())
list_length = int(input())
multiples_list = list()

for multiple in range(1, list_length + 1):
    multiples_list.append(multiple * factor)

print(multiples_list)