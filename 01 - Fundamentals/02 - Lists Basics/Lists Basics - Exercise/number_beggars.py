numbers = [int(number) for number in input().split(", ")]
beggars_count = int(input())
beggars_list = [0] * beggars_count

for index in range(len(numbers)):     
    beggars_list[index % beggars_count] += numbers[index]
    
print(beggars_list)