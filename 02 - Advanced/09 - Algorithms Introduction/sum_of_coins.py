from typing import List


def sum_coins(available_coins: List[int], desired_sum: int) -> str:
    available_coins.sort()

    coins_counts = {}
    total_coins = 0

    while desired_sum and available_coins:
        current_coin = available_coins.pop()

        used_coins, desired_sum = divmod(desired_sum, current_coin)

        if used_coins:
            total_coins += used_coins
            coins_counts[current_coin] = used_coins

    if desired_sum:
        return "Error"

    result = [
        f"Number of coins to take: {total_coins}",
        *(
            f"{count} coin(s) with value {coin}"
            for coin, count in coins_counts.items()
        )
    ]

    return "\n".join(result)


def main():
    available_coins = list(map(int, input().split(", ")))
    desired_sum = int(input())

    print(sum_coins(available_coins, desired_sum))


if __name__ == "__main__":
    main()
