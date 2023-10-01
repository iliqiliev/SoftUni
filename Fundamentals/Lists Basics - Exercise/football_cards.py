referees_notebook = input().split()
team_a = team_b = 11
sent_off_players = set()

for red_card in referees_notebook:
    if red_card not in sent_off_players:
        if red_card[0] == "A":
            team_a -= 1
        else:
            team_b -= 1
        sent_off_players.add(red_card)
    if team_a < 7 or team_b < 7:
        print(f"Team A - {team_a}; Team B - {team_b}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {team_a}; Team B - {team_b}")