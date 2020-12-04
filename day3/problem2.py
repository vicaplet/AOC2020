from functools import reduce

slopemap = None
with open('day3/input.txt') as superpointer:
    slopemap = superpointer.readlines()
    slopemap = [l.strip() for l in slopemap]

config = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2},
]

forest = []

for c in config:
    current_pos = 0
    trees = 0

    newmap = [l for i, l in enumerate(slopemap) if i >= c["down"]]

    for lindex, l in enumerate(newmap):
        if (lindex % c["down"]) != 0:
            continue
        
        next_pos = current_pos + c["right"]

        index = next_pos
        while (index + 1) > len(l):
            index -= len(l)

        if l[index] == '#':
            trees += 1
        current_pos = next_pos

    forest.append(trees)

print(forest)

result = reduce((lambda x, y: x * y), forest)

print(result)
