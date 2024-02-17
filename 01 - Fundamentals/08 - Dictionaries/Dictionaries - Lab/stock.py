elements = input().split()
bakery = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}

product_query = input().split()

for query in product_query:
    if query in bakery:
        print(f"We have {bakery[query]} of {query} left")

    else:
        print(f"Sorry, we don't have {query}")
