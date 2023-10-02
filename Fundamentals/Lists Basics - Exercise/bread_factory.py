events = [event.split('-') for event in input().split('|')]
energy = coins = 100

for event in events:
    event_type, event_amount = event[0], int(event[1])
    
    if event_type == "rest":
        if energy + event_amount > 100:
            event_amount = 100 - energy
        energy += event_amount
        print(f"You gained {event_amount} energy.")
        print(f"Current energy: {energy}.")
    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += event_amount
            print(f"You earned {event_amount} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_amount:
            coins -= event_amount
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            break
else:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")