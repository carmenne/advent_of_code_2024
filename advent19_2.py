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

def is_towel(tl, memo):

    if tl in memo:
        return memo[tl]

    if tl == "":
        return 1

    pos = 0
    for i in range(1, len(tl) + 1):
        sub_tl = tl[:i]
        if sub_tl in combs:

            pos += is_towel(tl[i:], memo)
    memo[tl] = pos

    return pos

possible = 0

memo = {}
for towel in towels:
    total = [0]
    all_towels = []
    sub_total = is_towel(towel, memo)
    possible += sub_total

print("Possible", possible) # 796449099271652
