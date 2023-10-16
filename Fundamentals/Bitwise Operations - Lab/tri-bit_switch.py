number = int(input())
position = int(input())

mask = 7 << position # mask is 111 (7) ending at the required position
switched_number = number ^ mask # when we xor it we flip the original number

print(switched_number)
