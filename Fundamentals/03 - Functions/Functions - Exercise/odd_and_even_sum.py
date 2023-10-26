def sum_per_parity(integer: int) -> str:
    
    integer_as_str = str(integer)
    odd_sum = even_sum = 0
    
    for digit in integer_as_str:
        if int(digit) & 1:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
           
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())

print(sum_per_parity(number))