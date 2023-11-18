tickets_to_check = [ticket.strip() for ticket in input().split(", ")]
winning_signs = ("@", "#", "$", "^")

for ticket in tickets_to_check:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    max_repeats = 0
    winning_sign = None

    for sign in winning_signs:
        repeats = 5
        # check how many repeats each sign has in both halves of the ticket
        while all(sign * (repeats + 1) in half for half in (ticket[:10], ticket[10:])):
            repeats += 1

        if repeats > max_repeats:
            max_repeats = repeats
            winning_sign = sign

    if max_repeats < 6:
        print(f'ticket "{ticket}" - no match')

    elif max_repeats < 10:
        print(f'ticket "{ticket}" - {max_repeats}{winning_sign}')

    else:
        print(f'ticket "{ticket}" - {max_repeats}{winning_sign} Jackpot!')
