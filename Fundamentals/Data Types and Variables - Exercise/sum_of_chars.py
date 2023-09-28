number_of_chars = int(input())
ascii_sum = 0

for _ in range(number_of_chars):
    character = input()
    ascii_sum += ord(character)

print(f"The sum equals: {ascii_sum}")