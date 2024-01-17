even_names = set()
odd_names = set()

for index in range(1, int(input()) + 1):
    name_score = sum(ord(char) for char in input()) // index

    if name_score & 1:
        odd_names.add(name_score)

    else:
        even_names.add(name_score)

even_sum = sum(even_names)
odd_sum = sum(odd_names)

# logic dies here
if odd_sum > even_sum:
    print(*(odd_names - even_names), sep=", ")

elif odd_sum < even_sum:
    print(*(odd_names ^ even_names), sep=", ")

else:
    print(*(odd_names | even_names), sep=", ")
