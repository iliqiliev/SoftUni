banned_words = input().split(", ")
text = input()

for banned_word in banned_words:
    while banned_word in text:
        text = text.replace(banned_word, "*" * len(banned_word))

print(text)
