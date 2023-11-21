import re

# Sofia phone number pattern
pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
valid_numbers = [match.group() for match in re.finditer(pattern, input())]

print(", ".join(valid_numbers))
