def alphabet_position(char: str) -> int:
    return ord(char.casefold()) - 96


def word_score(word: str) -> float:
    number = int(word[1:-1])
    before = word[0]
    after = word[-1]

    if before.isupper():
        number /= alphabet_position(before)
    else:
        number *= alphabet_position(before)

    if after.isupper():
        number -= alphabet_position(after)
    else:
        number += alphabet_position(after)

    return number


def main():
    game_words = input().split()
    total_sum = 0

    for word in game_words:
        total_sum += word_score(word)

    print(f"{total_sum:.2f}")


if __name__ == "__main__":
    main()
