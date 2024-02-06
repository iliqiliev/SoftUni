import os
from string import punctuation


script_directory = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_directory, "data", "text.txt")
output_path = os.path.join(os.path.dirname(input_path), "output.txt")

with open(input_path, encoding="utf-8") as file:
    text = file.readlines()

with open(output_path, "w", encoding="utf-8") as file:
    for index, line in enumerate(text, start=1):
        letters = marks = 0

        for character in line:
            if character.isalpha():
                letters += 1

            elif character in punctuation:
                marks += 1

        file.write(f"Line {index}: {line.rstrip()} ({letters})({marks})\n")
