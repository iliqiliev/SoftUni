clothes = [int(item) for item in input().split()]
current_rack_capacity = rack_capacity = int(input())
rack_counter = 1 if clothes else 0

while clothes:
    current_item = clothes.pop()

    if current_item <= current_rack_capacity:
        current_rack_capacity -= current_item

    else:
        rack_counter += 1
        current_rack_capacity = rack_capacity - current_item

print(rack_counter)
