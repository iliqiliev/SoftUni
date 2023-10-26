number_of_snowballs = int(input())
best_score = 0
best_weight = 0
best_airtime = 0
best_quality = 0

for _ in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_airtime = int(input())
    snowball_quality = int(input())
    snowball_score = (snowball_weight / snowball_airtime) ** snowball_quality

    if snowball_score > best_score:
        best_weight = snowball_weight
        best_airtime = snowball_airtime
        best_quality = snowball_quality
        best_score = snowball_score

print(f"{best_weight} : {best_airtime} = {best_score:.0f} ({best_quality})")