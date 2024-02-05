import os


script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "data", "text.txt")

try:
    print("Opening existing file:")
    with open(file_path, encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print(f"File {file_path} not found!")
