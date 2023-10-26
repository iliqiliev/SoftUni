needed_xp = float(input())
count_of_battles = int(input())
total_xp = 0
battle = 0

for battle in range(1, count_of_battles + 1):

    current_xp = float(input())
    total_xp += current_xp

    if battle % 3 == 0:  # every third day
        total_xp += (0.15 * current_xp)

    if battle % 5 == 0:  # every fifth day
        total_xp -= (0.10 * current_xp)

        if battle % 15 == 0:  # a day can only a fifteenth be if it is also a fifth
            total_xp += (0.05 * current_xp)

    if total_xp >= needed_xp:
        print(f"Player successfully collected his "
              f"needed experience for {battle} battles.")
        break

else:
    print(f"Player was not able to collect the needed "
          f"experience, {needed_xp - total_xp:.2f} more needed.")
