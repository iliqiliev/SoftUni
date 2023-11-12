from collections import defaultdict


contests_info = {}

while True:
    command = input().split(":")
    if len(command) != 2:
        break

    contest_name, contest_password = command
    contests_info[contest_name] = contest_password


submissions = defaultdict(dict)

while True:
    command = input().split("=>")
    if len(command) != 4:
        break

    contest_name, contest_password, username, points = command
    points = int(points)

    # if the provided password matches the one stored or None if password not stored
    if contests_info.get(contest_name, None) == contest_password:
        current = submissions[username]

        current[contest_name] = max(points, current.get(contest_name, 0))

# the best candidate is the one with the biggest sum of the inner dictionary values
# best is a tuple consisting of the name and the dictionary with the scores
best = max(submissions.items(), key=lambda score: sum(score[1].values()))
best_name, best_score = best[0], sum(best[1].values())

print(f"Best candidate is {best_name} with total {best_score} points.")
print("Ranking:")
for username, scores in sorted(submissions.items()):
    print(username)

    for contest, points in sorted(scores.items(), key=lambda score: -score[1]):
        print(f"#  {contest} -> {points}")
