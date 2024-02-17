#       title    content
body = [input(), input()]
#                comment
body.extend(iter(input, "end of comments"))

print(f"<h1>\n\t{body[0]}\n</h1>")
print(f"<article>\n\t{body[1]}\n</article>")
for comment in body[2:]:
    print(f"<div>\n\t{comment}\n</div>")

# Just for fun:
# print(f"<h1>\n\t{input()}\n</h1>\n<article>\n\t{input()}\n</article>\n" + "\n".join(f"<div>\n\t{comment}\n</div>" for comment in list(iter(input, "end of comments"))))
