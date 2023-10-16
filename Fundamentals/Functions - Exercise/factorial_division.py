import math

def factorial_division(x: int, y: int) -> float:
    
    fac_x = math.factorial(x)
    fac_y = math.factorial(y)

    return fac_x / fac_y
    
    
number_1, number_2 = int(input()), int(input())
print(f"{factorial_division(number_1, number_2):.2f}")