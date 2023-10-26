number_of_pours = int(input())
tank_capacity = 255

for _ in range(number_of_pours):
    pour = int(input())
    if pour > tank_capacity:
        print("Insufficient capacity!")
    else:
        tank_capacity -= pour

print(255 - tank_capacity)