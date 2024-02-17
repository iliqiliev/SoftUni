import re


sentence = input()
target_word = input()

# fr fr
matches = re.findall(rf"\b{target_word}\b", sentence, re.IGNORECASE)

print(len(matches))
