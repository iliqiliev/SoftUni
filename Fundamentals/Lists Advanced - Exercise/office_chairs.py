number_of_rooms = int(input())
free_chairs = 0
game_on = True

for room in range(1, number_of_rooms + 1):
    
    chairs, visitors = input().split()    
    surplus = len(chairs) - int(visitors)
    free_chairs += surplus
    
    if surplus < 0:
        print(f"{-surplus} more chairs needed in room {room}" * (surplus < 0))
        game_on = False
         
if game_on:
    print(f"Game On, {free_chairs} free chairs left")