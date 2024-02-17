import re


full_name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
full_names = re.findall(full_name_pattern, input())

print(" ".join(full_names))
