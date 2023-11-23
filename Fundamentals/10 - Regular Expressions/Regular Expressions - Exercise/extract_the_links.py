import re
import sys


links_pattern = r"www\.[A-Za-z][A-Za-z\d-]+[A-Za-z\d](?:\.[A-Z|a-z]{2,})+"

text = sys.stdin.read()
links = re.findall(links_pattern, text)

print("\n".join(links))
