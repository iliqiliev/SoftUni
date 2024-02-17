import re


demon_info = {}

demon_name_pattern = r"[^\s,]+"
demon_health_pattern = re.compile(r"[^\d\+\-\*\/\.]")
demon_damage_pattern = re.compile(r"-?\d+(?:\.\d+)?")

for demon_name in re.findall(demon_name_pattern, input()):
    demon_health = sum(ord(char) for char in demon_health_pattern.findall(demon_name))

    demon_damage = sum(float(num) for num in demon_damage_pattern.findall(demon_name))
    demon_damage *= 2 ** (demon_name.count("*"))
    demon_damage /= 2 ** (demon_name.count("/"))

    demon_info[demon_name] = (demon_health, demon_damage)

for demon_name, demon_stats in sorted(demon_info.items()):
    print(f"{demon_name} - {demon_stats[0]} health, {demon_stats[1]:.2f} damage")
