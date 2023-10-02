input_fire = input().split("#")
input_fire = [x.split(" = ") for x in input_fire]

available_water = int(input())
effort = 0.0
fire_put_out = 0

fires_info = {
    "High": (81, 125),
    "Medium": (51, 80),
    "Low": (1, 50)
}

print("Cells:")
for fire in input_fire:
    fire_type, fire_level = fire[0], int(fire[1])
    min_fire, max_fire = fires_info[fire_type]
    if fire_type in fire and \
       min_fire <= fire_level <= max_fire and \
       available_water >= fire_level:
           
        available_water -= fire_level
        effort += 0.25 * fire_level
        fire_put_out += fire_level
        print(f" - {fire_level}")  
        
print(f"Effort: {effort:.2f}\n"
      f"Total Fire: {fire_put_out}")