import os


script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "data", "text.txt")

old_chars = "-,.!?"
new_char = input("Enter a replacement character: ") or chr(0)

replacement_table = {ord(char): ord(new_char) for char in old_chars}

with open(file_path, encoding="utf-8") as file:
    text = file.readlines()

for row_index in range(0, len(text), 2):
    row = text[row_index].translate(replacement_table).split()
    print(" ".join(reversed(row)))
