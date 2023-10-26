original_sentence = input().split(", ")
checking_sentence = input().split(", ")
substrings = []

for word in original_sentence:
    for check in checking_sentence:
        if word in check:
            substrings.append(word)
            break
            
print(substrings)