def negative_vs_positive(*numbers: int) -> None:
    negative = positive = 0

    for number in numbers:
        if number > 0:
            positive += number

        else:
            negative += number

    print(negative, positive, sep="\n")
    if abs(negative) > positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = map(int, input().split())
negative_vs_positive(*nums)
