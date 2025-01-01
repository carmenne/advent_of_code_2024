import sys

sys.setrecursionlimit(10000)
tokens = []
all_counts = []

with open("input_long.txt", "r") as file:
    for line in file:
        token, cts = line.strip().split(" ")
        tokens.append(token.strip("."))
        all_counts.append([int(c) for c in cts.split(",")])

total = 0

seen = set()

def get_len(counts):
    return sum(counts) + len(counts) - 1

def valid(token, counts):
    sub_tokens = [s_t for s_t in token.split(".") if s_t != ""]
    if len(sub_tokens) != len(counts):
        return False

    sub_tokens_len = [len(t) for t in sub_tokens]
    return sub_tokens_len == counts

memo={}
def solve(token, counts):
    if "?" not in token:
        return 1 if valid(token, counts) else 0

    result = 0
    i = token.find("?")
    solve1 = solve(token[:i] + "." + token[i + 1:], counts)
    solve2 = solve(token[:i] + "#" + token[i + 1:], counts)
    result += solve1 + solve2

    return result

token = 0
for token, counts in zip(tokens, all_counts):
    res = solve(token, counts)
    total += res

print(total) # 7204