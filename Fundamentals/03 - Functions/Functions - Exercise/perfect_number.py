def perfect_number(number: int) -> str:
    
    divisors = list()
    
    for i in range(1, int(number**0.5) + 1):  
        if number % i == 0:          
            if (number / i == i):
                divisors.append(i)
            else:              
                divisors.extend([i, int(number / i)])
                
    is_perfect = int(sum(divisors) / 2) == number
                
    if is_perfect:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."
 
               
number = int(input())   
print(perfect_number(number))