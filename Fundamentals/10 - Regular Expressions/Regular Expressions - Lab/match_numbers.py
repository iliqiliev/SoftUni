import re


numeric_regex = r"(^|(?<=\s))-?([0]|[1-9][\d]*)(\.?\d+)?($|(?=\s))"

for number in re.finditer(numeric_regex, input()):
    print(number.group(), end=" ")
