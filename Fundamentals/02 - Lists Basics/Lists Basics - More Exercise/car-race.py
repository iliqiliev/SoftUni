car_times = [int(time) for time in input().split()]
middle = (len(car_times) - 1) // 2

left_car_times = car_times[:middle] # first half
right_car_times = car_times[:middle:-1] # first half reversed
left_car_total_time = right_car_total_time = 0

for left_time, right_time in zip(left_car_times, right_car_times):    
    if not left_time:
        left_car_total_time *= 0.8
    if not right_time:
        right_car_total_time *= 0.8
        
    left_car_total_time += left_time
    right_car_total_time += right_time
        
winner = "left" * (left_car_total_time < right_car_total_time) + \
         "right" * (left_car_total_time > right_car_total_time) # branchless 8)
              
print(f"The winner is {winner} with total time: {locals()[winner + '_car_total_time']:.1f}") # was curious 