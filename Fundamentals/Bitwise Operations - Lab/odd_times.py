times = [int(x) for x in input().split()]

result = 0
for time in times: # every pair of numbers "destroys" itself because of the bitwise XOR
    result ^= time
    
print(result)