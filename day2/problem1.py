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
    rule_min = int(results.group(1))
    rule_max = int(results.group(2))
    rule_char = results.group(3)
    pwd_string = results.group(4)

    occurences = pwd_string.count(rule_char)
    if occurences >= rule_min and occurences <= rule_max:
        counter += 1

print(counter)

