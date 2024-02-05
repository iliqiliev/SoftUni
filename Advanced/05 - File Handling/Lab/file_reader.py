import os


script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "data", "numbers.txt")

with open(file_path, encoding="utf-8") as file:
    numbers_sum = sum(int(line.strip()) for line in file.readlines())

print(numbers_sum)
