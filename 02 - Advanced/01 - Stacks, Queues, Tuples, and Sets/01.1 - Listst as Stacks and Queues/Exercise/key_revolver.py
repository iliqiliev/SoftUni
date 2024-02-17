from collections import deque


bullet_price = int(input())
barrel_current = barrel_size = int(input())
bullets = deque(int(bullet_size) for bullet_size in input().split())

locks = deque(int(lock_size) for lock_size in input().split())
target_value = int(input())

while bullets and locks:
    bullet_current = bullets.pop()
    barrel_current -= 1
    target_value -= bullet_price

    if bullet_current <= locks[0]:  # can open
        locks.popleft()
        print("Bang!")

    else:  # can't open
        print("Ping!")

    if not barrel_current and bullets:
        barrel_current = min(barrel_size, len(bullets))
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${target_value}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
