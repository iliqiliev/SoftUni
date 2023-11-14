sentence = input().split()

for word in sentence:
    print(word * len(word), end="")
