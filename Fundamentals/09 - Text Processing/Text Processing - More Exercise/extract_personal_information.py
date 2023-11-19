for _ in range(int(input())):
    data = input()

    name = data[data.index("@") + 1 : data.index("|")]
    age = data[data.index("#") + 1 : data.index("*")]

    print(f"{name} is {age} years old.")
