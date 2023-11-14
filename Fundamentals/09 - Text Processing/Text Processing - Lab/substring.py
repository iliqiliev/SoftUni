undesirable = input()
string = input()

while undesirable in string:
    string = string.replace(undesirable, "")

print(string)
