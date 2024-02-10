from mathematical_operations import generate_fibonacci, fibonacci_index


sequence = []

while len(command := input("Enter command: ").split()) > 1:
    operation, number = command[0], int(command[-1])

    if operation == "Create":
        sequence = generate_fibonacci(number)
        print(*sequence)

    elif operation == "Locate":
        if index := fibonacci_index(number, sequence):
            print(f"The number - {number} is at index {index}")

        else:
            print(f"The number {number} is not in the sequence.")
