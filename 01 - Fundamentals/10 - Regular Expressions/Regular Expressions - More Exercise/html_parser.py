import re


html_pattern = r"<title>(.*)</title>.*<body>(.*)</body>"
tag_pattern = r"<.*?>"

html_match = re.search(html_pattern, input())

if html_match:
    title, body = html_match.groups()
    content = re.sub(tag_pattern, "", body).replace(R"\n", "")

    print(f"Title: {title}")
    print(f"Content: {content}")
