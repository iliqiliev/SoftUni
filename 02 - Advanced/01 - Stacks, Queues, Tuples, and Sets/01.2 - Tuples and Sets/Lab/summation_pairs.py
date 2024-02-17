numbers = {int(num) for num in input().split()}
sum_target = int(input())
checked = set()

for number in numbers:
    difference = sum_target - number

    if difference in checked:
        print(f"{number} + {difference} = {sum_target}")

    checked.add(number)
