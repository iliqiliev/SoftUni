input_fire = input().split("#")
input_fire = [x.split(" = ") for x in input_fire]

input_water = int(input())
effort = 0.0
fire_put_out = 0

print("Cells:")
for fire in input_fire:
    fire[1] = int(fire[1])
    if (fire[0] == "High" and 80 < fire[1] <= 125 or \
       fire[0] == "Medium" and 50 < fire[1] <= 80 or \
       fire[0] == "Low" and 0 < fire[1] <= 50) and \
       input_water >= fire[1]:
           
        input_water -= fire[1]
        effort += 0.25 * fire[1]
        fire_put_out += fire[1]
        print(f" - {fire[1]}")  
        
print(f"Effort: {effort:.2f}\n"
      f"Total Fire: {fire_put_out}")