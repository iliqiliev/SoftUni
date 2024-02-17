from collections import deque


boxes = [int(box) for box in input().split()]
magic_values = deque(int(magic) for magic in input().split())

toys = {
    "Doll": {"price": 150, "count": 0},
    "Wooden train": {"price": 250, "count": 0},
    "Teddy bear": {"price": 300, "count": 0},
    "Bicycle": {"price": 400, "count": 0},
}

prices = {toy_info["price"]: toy for toy, toy_info in toys.items()}

while boxes and magic_values:
    current_box = boxes.pop()
    current_magic = magic_values.popleft()

    total_magic = current_box * current_magic
    if total_magic in prices:
        toys[prices[total_magic]]["count"] += 1

    elif total_magic < 0:
        boxes.append(current_box + current_magic)

    elif total_magic > 0:
        boxes.append(current_box + 15)

    else:
        if current_box:
            boxes.append(current_box)

        if current_magic:
            magic_values.appendleft(current_magic)

if (toys["Doll"]["count"] and toys["Wooden train"]["count"] or
        toys["Teddy bear"]["count"] and toys["Bicycle"]["count"]):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if boxes:
    print("Materials left:", ", ".join(str(box) for box in reversed(boxes)))

if magic_values:
    print("Magic left:", ", ".join(str(magic) for magic in magic_values))

for toy, toy_info in sorted(toys.items()):
    if toy_info["count"]:
        print(f"{toy}: {toy_info['count']}")
