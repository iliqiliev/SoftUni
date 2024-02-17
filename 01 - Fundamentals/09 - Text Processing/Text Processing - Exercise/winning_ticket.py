def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"

    for sign in ("@", "#", "$", "^"):
        for repeats in range(10, 5, -1):
            # check both halves of the ticket
            if all(sign * repeats in half for half in (ticket[:10], ticket[10:])):
                # add jackpot to the string only if the number of repeats is 10
                return f'ticket "{ticket}" - {repeats}{sign}' + (
                    " Jackpot!" * (repeats == 10)
                )

    return f'ticket "{ticket}" - no match'


tickets_to_check = [ticket.strip() for ticket in input().split(", ")]

for current_ticket in tickets_to_check:
    print(check_ticket(current_ticket))
