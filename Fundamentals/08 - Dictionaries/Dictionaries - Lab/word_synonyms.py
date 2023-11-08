from collections import defaultdict

number_of_pairs = int(input())
dictionary = defaultdict(list)

for pair in range(number_of_pairs):
    #          word            synonym
    dictionary[input()].append(input())

for word, synonyms in dictionary.items():
    print(f"{word} - {', '.join(synonyms)}")
