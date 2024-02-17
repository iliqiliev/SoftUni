def sum_numbers(int1: int, int2: int) -> int:
    return int1 + int2


def subtract(int1: int, int2: int) -> int:
    return int1 - int2


def add_and_subtract(int1: int, int2: int, int3: int) -> int:
    return subtract(sum_numbers(int1, int2), int3)


integer1 = int(input())
integer2 = int(input())
integer3 = int(input())

print(add_and_subtract(integer1, integer2, integer3))