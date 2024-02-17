from math import log, e


number = int(input("Enter number: "))

try:
    base = int(input("Enter base: "))

except ValueError:
    base = e

print(f"Exponent: {log(number, base):.2f}")
