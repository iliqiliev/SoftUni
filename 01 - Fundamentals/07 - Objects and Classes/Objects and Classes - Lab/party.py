class Party:

    def __init__(self) -> None:
        self.people = []


party = Party()

command = input()
while command != "End":
    party.people.append(command)
    
    command = input()

print(f"Going: {', '.join(party.people)}\n"
      f"Total: {len(party.people)}")