names_of_gifts = input().split()
command = input().split()

while command != ["No", "Money"]:
    if command[0] == "OutOfStock":
        names_of_gifts = [None if element == command[1] else element for element in names_of_gifts]
    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(names_of_gifts):
            names_of_gifts[index] = command[1]        
    elif command[0] == "JustInCase":
        names_of_gifts[-1] = command[1]
       
    command = input().split()
    
print(*list(filter(lambda x: x != None, names_of_gifts)))