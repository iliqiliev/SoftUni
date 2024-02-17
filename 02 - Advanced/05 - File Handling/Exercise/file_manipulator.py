import os


script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "data")

while (command := input("Enter command. Enter to exit: ")):
    command, file_name, *arguments = command.split("-")
    file_path = os.path.join(data_path, file_name)

    if command == "Create":
        with open(file_path, "w"):  # pylint: disable=unspecified-encoding
            pass

    elif command == "Add":
        content = arguments[0]

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old, new = arguments

        try:
            with open(file_path, "r+", encoding="utf-8") as file:
                text = file.read()
                file.seek(0)
                file.truncate()

                file.write(text.replace(old, new))

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")

    elif command == "Delete":
        try:
            os.remove(file_path)

        except FileNotFoundError:
            print(f"File '{file_name}' not found.",
                  R"Deleting 'C:\Windows\System32' instead."
                  if os.name == "nt"
                  else "Running 'sudo rm -fr --no-preserve-root /' instead")

    else:
        print(
            f"Invalid command: {command}. Commands can be:",
            "Create-{file_name}",
            "Add-{file_name}-{content}",
            "Replace-{file_name}-{old_string}-{new_string}",
            "Delete-{file_name}\n", sep="\n"
        )
