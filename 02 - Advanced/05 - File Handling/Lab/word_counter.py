import os
import re


script_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(script_directory, "data")

with open(os.path.join(data_directory, "input.txt"), encoding="utf-8") as file:
    text = file.read()

print(f"Text:\n{text}")
searched_words = input("Enter words to be searched in the text: ").split()

counts = {word: len(re.findall(fr"\b{word}\b", text, re.IGNORECASE))
          for word in searched_words}

with open(
    os.path.join(data_directory, "output.txt"),
    mode="w",
    encoding="utf-8"
) as file:
    for word, occurrences in sorted(counts.items(), key=lambda kvp: -kvp[1]):
        file.write(f"{word} - {occurrences}\n")
