import sys

sys.setrecursionlimit(10000)
tokens = []
all_counts = []

with open("input_long.txt", "r") as file:
    for line in file:
        token, cts = line.strip().split(" ")
        strip = token.strip("")

        tokens.append("?".join([strip]*5))
        all_counts.append([int(c) for c in cts.split(",")]*5)

total = 0

memo={}
def solve(token, counts):
    if not counts:
        return 1 if "#" not in token else 0
    if not token:
        return not counts

    key = token, ",".join([str(c) for c in counts])
    if key in memo:
        return memo[key]

    i = token[0]
    if i == ".":
        result = solve(token[1:], counts)
    elif i == "#":
        new_counts = counts.copy()
        to_remove = counts[0]
        if (len(token) >= to_remove
                and "." not in token[0:to_remove]
                and (len(token) == to_remove or token[to_remove] in ".?")):
            new_counts.remove(to_remove)
            result = solve(token[to_remove+1:], new_counts.copy())
        else:
            result = 0
    else:
        solve1 = solve("." + token[1:], counts)
        solve2 = solve("#" + token[1:], counts)
        result = solve1 + solve2

    memo[token, ",".join([str(c) for c in counts])] = result

    return result

token = 0
for token, counts in zip(tokens, all_counts):
    res = solve(token, counts)
    total += res

print(total)  # 1672318386674
