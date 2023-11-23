import re


text = input()
email_pattern = r"""
    (?<!\S) # ensure no not-whitespace in the front
    (?:[A-Za-z0-9]+[-._])*[A-Za-z0-9]+ # first and last can only be letter or digit
    @[A-Za-z-]+ # root domain
    (?:\.[A-Z|a-z]{2,}){1,2} # top and/or second level domain
    """

email_addresses = re.findall(email_pattern, text, re.VERBOSE)
print("\n".join(email_addresses))
