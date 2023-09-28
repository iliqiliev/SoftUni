import math

number_of_people = int(input())
elevator_capacity = int(input())

total_trips = math.ceil(number_of_people / elevator_capacity)

print(total_trips)