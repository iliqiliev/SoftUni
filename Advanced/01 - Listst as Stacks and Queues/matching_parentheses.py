parentheses_positions = []
expression = input()

for index, character in enumerate(expression):
    if character == "(":
        parentheses_positions.append(index)

    elif character == ")":
        print(expression[parentheses_positions.pop():index + 1])
