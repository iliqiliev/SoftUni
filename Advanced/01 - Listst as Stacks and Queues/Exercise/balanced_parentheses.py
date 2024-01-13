left_side = []
sequence = input()

for char in sequence:
    if char in "([{":
        left_side.append(char)

    elif not left_side or left_side.pop() + char not in ("()", "[]", "{}"):
        print("NO")
        break

else:
    print("YES")
