days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plunder = 0

for day in range(1, days + 1):
    
    plunder += daily_plunder
    
    if not (day % 3):
        plunder += daily_plunder * 0.5
        
    if not (day % 5):
        plunder -= (plunder * 0.3)

if plunder >= expected_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
    
else:
    plunder_percentage = (plunder / expected_plunder) * 100
    print(f"Collected only {plunder_percentage:.2f}% of the plunder.")
