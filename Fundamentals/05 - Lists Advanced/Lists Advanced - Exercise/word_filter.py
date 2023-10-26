even_words = [word for word in input().split() if not (len(word) & 1)]

print(*even_words, sep="\n")