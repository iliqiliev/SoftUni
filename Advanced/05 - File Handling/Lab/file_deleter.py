import os


file_name = input("Enter file name for deletion: ")

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "data", file_name)

try:
    os.remove(file_path)

except FileNotFoundError:
    print(f"{file_path} does not exist!")
