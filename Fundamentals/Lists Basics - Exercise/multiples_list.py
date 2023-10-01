factor = int(input())
list_length = int(input())
multiples_list = list()

for multiple in range(factor, (list_length * factor) + 1, factor):
    multiples_list.append(multiple)

print(multiples_list)