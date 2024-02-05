import os


file_name = input("Enter file name for creation: ")

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "data", file_name)

with open(file_path, "w", encoding="utf-8") as file:
    file.write(input(f"Enter {file_name} contents: "))
