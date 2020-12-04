slopemap = None
with open('day3/input.txt') as superpointer:
    slopemap = superpointer.readlines()
    slopemap = [l.strip() for l in slopemap]

current_pos = 0
trees = 0

del slopemap[0]

for l in slopemap:
    next_pos = current_pos + 3

    index = next_pos
    while (index + 1) > len(l):
        index -= len(l)

    if l[index] == '#':
        trees += 1
    current_pos = next_pos

print(trees)