import sys
import re

text = sys.stdin.read()
numbers = re.findall(r"\d+", text)

print(*numbers)
