message = input().split()
message_deciphered = list()

for word in message:

    ascii_length = sum(char.isdigit() for char in word)  # count digits
    # get first digits from the upper var
    first_letter = chr(int(word[:ascii_length]))

    # convert word to list with final length
    word_deciphered = list(word[ascii_length - 1:])

    # first letter is now the letter from the ascii table
    word_deciphered[0] = first_letter
    # switch the 2nd and the last character
    word_deciphered[1], word_deciphered[-1] = word_deciphered[-1], word_deciphered[1]

    message_deciphered.append("".join(word_deciphered))


print(*message_deciphered, sep=" ")
