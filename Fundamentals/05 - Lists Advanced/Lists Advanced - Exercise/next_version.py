old_version = int(input().replace(".", "")) # remove dots so we can convert to int
new_version = str(old_version + 1) # add 1 and then convert to str so we can unpack with *

print(*new_version, sep=".")