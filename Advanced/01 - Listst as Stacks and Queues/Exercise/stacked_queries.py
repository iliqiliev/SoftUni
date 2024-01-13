stack = []
number_of_queries = int(input())

for _ in range(number_of_queries):
    query, *number = input().split()

    if query == "1":
        stack.append(int(number[0]))

    if stack:
        if query == "2":
            stack.pop()

        elif query == "3":
            print(max(stack))

        elif query == "4":
            print(min(stack))

print(*reversed(stack), sep=", ")
