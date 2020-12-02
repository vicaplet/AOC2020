import re

bamboogrove = None
with open('./day2/input.txt') as superpointer:
    bamboogrove = superpointer.readlines()
    bamboogrove = [l.strip() for l in bamboogrove]

counter = 0

for bamboo in bamboogrove:
    results = re.match(r"^(\d+)-(\d+) (\D): (\w+)$", bamboo)
    if results is None:
        continue
    rule_pos1 = int(results.group(1))
    rule_pos2 = int(results.group(2))
    rule_char = results.group(3)
    pwd_string = results.group(4)

    if (rule_char == pwd_string[rule_pos1 - 1] or rule_char == pwd_string[rule_pos2 - 1]) and (pwd_string[rule_pos1 - 1] != pwd_string[rule_pos2 - 1]):
        counter += 1

print(counter)

