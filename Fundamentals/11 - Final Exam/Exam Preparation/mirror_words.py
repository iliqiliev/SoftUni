import re


mirrored_pair_pattern = r"""
    (?P<sep>[@|#])
    (?P<word_first>[A-Za-z]{3,})
    (?P=sep){2}
    (?P<word_second>[A-Za-z]{3,})
    (?P=sep)
    """

word_pairs = re.findall(mirrored_pair_pattern, input(), re.VERBOSE)
if word_pairs:
    print(f"{len(word_pairs)} word pairs found!")

    palindromes = [
        f"{word_pair[1]} <=> {word_pair[2]}" for word_pair in word_pairs
        if word_pair[1] == word_pair[2][::-1]
    ]

    if palindromes:
        print(f"The mirror words are:\n{', '.join(palindromes)}")

    else:
        print("No mirror words!")


else:
    print("No word pairs found!")
    print("No mirror words!")
