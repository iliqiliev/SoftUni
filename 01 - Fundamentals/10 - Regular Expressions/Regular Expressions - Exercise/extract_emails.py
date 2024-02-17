import re


email_pattern = r"""
    (?<=\s) # ensure whitespace character in the front
    (?:[A-Za-z0-9]+[-._])*[A-Za-z0-9]+ # first and last can only be letter or digit
    @[A-Za-z-]+ # root domain
    (?:\.[A-Z|a-z]{2,}){1,2} # top and/or second level domain
    """

email_addresses = re.findall(email_pattern, input(), re.VERBOSE)
print("\n".join(email_addresses))
