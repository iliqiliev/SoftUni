integer_list = [int(x) for x in input().split(", ")]

for integer in integer_list:
    if not integer:
        integer_list.append(0)
        integer_list.remove(0)
        
print(integer_list)