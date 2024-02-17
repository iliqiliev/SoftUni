def concatenate(*words: str, **replacements: str) -> str:
    concatenated = "".join(words)

    for word, replacement in replacements.items():
        concatenated = concatenated.replace(word, replacement)

    return concatenated
