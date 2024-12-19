import sys

sys.setrecursionlimit(10000)
towels = []
with open("input/advent19.txt", "r") as file:
    for l in file:
        line = l.strip()
        if "," in line:
            combs = set(line.replace(" ", "").split(","))
        elif line != "":
            towels.append(line)

print(combs)

def is_towel(tl):
    if tl in combs:
        return True

    pos = False
    for i in range(1, len(tl)):
        print(i, tl[:i])
        pos = tl[:i] in combs and is_towel((tl[i:]))
        if pos:
            return True

    return pos

possible = 0
for towel in towels:
    if is_towel(towel):

        print("is towel", towel)
        possible += 1

print("Possible", possible)
