people_in_the_circle = input().split()
suicide_step = int(input()) - 1
to_be_killed = suicide_step % len(people_in_the_circle)
killed = list()

while people_in_the_circle:
    killed.append(people_in_the_circle.pop(to_be_killed))
    if len(people_in_the_circle):
        to_be_killed = (to_be_killed + suicide_step) % len(people_in_the_circle)
        
print("[", end="")        
print(*killed, sep=",", end="]")