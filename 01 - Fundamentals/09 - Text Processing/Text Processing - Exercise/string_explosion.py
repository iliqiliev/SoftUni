text = list(input())

explosion_surplus = 0
index = 0
while index < len(text) - 1:
    current_char = text[index]

    if current_char == ">":
        explosion_strength = int(text[index + 1]) + explosion_surplus

        for removal_char in range(explosion_strength):
            # the index to be exploded
            exploding = index + 1

            #  avoids IndexError         stacking explosions
            if exploding >= len(text) or text[exploding] == ">":
                explosion_surplus = explosion_strength
                break

            # lower the explosion strength for the surplus calculation
            explosion_strength -= 1
            # boom
            del text[exploding]

    index += 1

print("".join(text))
