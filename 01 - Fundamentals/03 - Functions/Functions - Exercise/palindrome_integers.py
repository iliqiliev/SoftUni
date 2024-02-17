def is_palindrome(integers: str) -> list:
    
    output = list()
    
    for integer in integers.split(", "):
        if integer == integer[::-1]:
            output.append(True)
        else:
            output.append(False)    
                   
    return output  
        
    
number_list = input()
print(*is_palindrome(number_list), sep="\n")