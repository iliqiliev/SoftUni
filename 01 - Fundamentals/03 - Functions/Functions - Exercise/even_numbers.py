def is_even(integer: int) -> bool:
    return (not integer % 2)


number_list = [int(x) for x in input().split()]
even_number_list = list(filter(is_even, number_list))

print(even_number_list)