import sys
list_of_integers = [int(x) for x in input().split()]
command = input().split()

while command[0] != "end":
 
    if command[0] == "exchange":
        index = int(command[1])
        
        if 0 <= index < len(list_of_integers):
            new_first_half = list_of_integers[index + 1:]
            new_second_half = list_of_integers[:index + 1]
            list_of_integers = new_first_half + new_second_half
        else:
            print("Invalid index")
    
    elif command[0] in ("max", "min"):
        target_value = -sys.maxsize if command[0] == "max" else sys.maxsize
        target_index = None

        for index, integer in enumerate(list_of_integers):
            if (command[1] == "odd" and (integer % 2)) or \
               (command[1] == "even" and not (integer % 2)):
                if (command[0] == "min" and integer <= target_value) or \
                   (command[0] == "max" and integer >= target_value):
                    target_value = integer
                    target_index = index

        if target_index is not None:
            print(target_index)
        else:
            print("No matches")
                                  
    elif command[0] in ("first", "last"):        
        target_count = int(command[1])  
             
        if target_count <= len(list_of_integers):                    
            if command[2] == "odd":
                temp_list = [odd_number for odd_number in list_of_integers if odd_number % 2]
            else:
                temp_list = [even_number for even_number in list_of_integers if not (even_number % 2)]
                
            print(temp_list[-target_count:] if command[0] == "last" else temp_list[:target_count])                                          
        else:
            print("Invalid count")
        
    command = input().split()
    
else:
    print(list_of_integers)