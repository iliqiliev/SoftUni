class ValueCannotBeNegativeError(Exception):
    pass


for _ in range(5):
    value = int(input())

    if value < 0:
        raise ValueCannotBeNegativeError(value)
