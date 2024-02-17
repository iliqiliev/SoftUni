import re


star_enigma = re.compile(r"[star]", re.IGNORECASE)
message_pattern = re.compile(
    r"""
    @(?P<planet>[A-Za-z]+)[^@!:>\-]* 
    :(?P<population>\d+)[^@!:>\-]* 
    !(?P<type>A|D)![^@!:>\-]* 
    ->(?P<soldiers>\d+)
    """,
    re.VERBOSE,
)

planets = {"A": [], "D": []}

for _ in range(int(input())):
    encrypted_message = input()

    cypher_shift = len(star_enigma.findall(encrypted_message))

    decrypted_message = "".join(
        [chr(ord(char) - cypher_shift) for char in encrypted_message]
    )

    valid_message = message_pattern.search(decrypted_message)
    if valid_message:
        planets[valid_message["type"]].append(valid_message["planet"])

print(f"Attacked planets: {len(planets['A'])}")
for name in sorted(planets["A"]):
    print(f"-> {name}")
print(f"Destroyed planets: {len(planets['D'])}")
for name in sorted(planets["D"]):
    print(f"-> {name}")
