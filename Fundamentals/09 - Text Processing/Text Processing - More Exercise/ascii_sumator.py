start = ord(input())
end = ord(input())
text = input()
ascii_sum = 0

for character in text:
    if start < ord(character) < end:
        ascii_sum += ord(character)

print(ascii_sum)
