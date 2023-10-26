number = int(input())
position = int(input())

mask = ~(1 << position) # shift one the required positions and then flip it
number_destroyed = number & mask # so that bitwise and will return the original number except the zero

print(number_destroyed)