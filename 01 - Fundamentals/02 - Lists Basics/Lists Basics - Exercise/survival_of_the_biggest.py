list_of_integers = [int(number) for number in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))
    
print(*list_of_integers, sep=", ")