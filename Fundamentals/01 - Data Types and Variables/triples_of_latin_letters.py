letters = int(input())

for first_letter in range(letters):
    for second_letter in range(letters):
        for third_letter in range(letters):
            print(f"{chr(first_letter + 97)}{chr(second_letter + 97)}{chr(third_letter + 97)}")
            # 97 is the ascii index of a