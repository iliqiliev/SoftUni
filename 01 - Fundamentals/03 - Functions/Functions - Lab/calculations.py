def calculations(operator: str, a: int, b: int) -> int:
    return {
        "multiply": a * b,
        "divide": int(a / b),
        "add": a + b,
        "subtract": a - b,       
    }.get(operator, 0)
    
operation = input()
num1 = int(input())
num2 = int(input())
result = calculations(operation, num1, num2)

print(result)