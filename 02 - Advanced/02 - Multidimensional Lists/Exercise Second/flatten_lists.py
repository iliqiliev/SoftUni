flattened_list = [num
                  for sublist in input().split("|")[::-1]
                  for num in sublist.split()]

print(*flattened_list)
