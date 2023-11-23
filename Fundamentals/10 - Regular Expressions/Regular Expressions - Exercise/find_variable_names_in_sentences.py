import re


sentence = input()
variable_pattern = r"\b_([A-Za-z0-9]+)\b"

variables = re.findall(variable_pattern, sentence)
print(",".join(variables))
