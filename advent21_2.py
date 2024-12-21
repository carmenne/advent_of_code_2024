import sys

sys.setrecursionlimit(10000)

numeric = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["-1", "0", "A"]]
directional = [["-1", "^", "A"], ["<", "v", ">"]]
direct_to = {
    (0, -1): "<",  # left
    (-1, 0): "^",  # up
    (0, 1): ">",  # right
    (1, 0): "v",  # down
}
directions = [
    (0, -1),  # left
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
]

def in_bounds(x, y, M):
    if M == 4:
        return 0 <= x <= 3 and 0 <= y <= 2 and (x, y) != (3, 0)
    elif M == 2:
        return 0 <= x <= 1 and 0 <= y <= 2 and (x, y) != (0, 0)
    return False


def explore_paths_numeric(start, end, cost, M):
    queue = [(start[0], start[1], cost, 0, [])]
    min_steps = float('inf')
    memo = {}

    all_steps = []
    while queue:
        i, j, cost, dir, steps = queue.pop(0)
        if i == end[0] and j == end[1]:
            if cost < min_steps:
                min_steps = cost
            if min_steps == cost:
                return steps

        if (i, j) in memo and memo[(i, j)] < cost:
            continue

        memo[(i, j)] = cost

        if M == 4:
            if start[0] == 3 and end[1] == 0: # A - 7
                dir = 1 # up
            elif start[1] == 0 and end[0] == 3: # 7 - A
                dir = 2 # down
        elif M == 2:
            if start[0] == 0 and end[1] == 0:
                dir = 2
        for d in [0, 1, 2, 3]:
            new_dir = (dir + d) % 4
            di, dj = directions[new_dir]
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj, M):
                new_steps = steps.copy()
                new_steps.append((di, dj))
                queue.append((ni, nj, cost + 1, new_dir, new_steps))

    return all_steps


def get_numeric(move):
    number = "0"
    for m in move:
        if m in "123456789" or (m == "0" and numeric != "0"):
            number += m
    return int(number)


def get_idx(n):
    for i in range(4):
        for j in range(3):
            if in_bounds(i, j, 4) and numeric[i][j] == n:
                return i, j


def get_idx_robo(n):
    for i in range(2):
        for j in range(3):
            if in_bounds(i, j, 2) and directional[i][j] == n:
                return i, j


memo = {}


def expand(path, it, limit):

    if it == limit:
        return len(path)

    nr = 0
    for k in range(0, len(path)):
        ch = path[k]
        prev_ch = path[k - 1] if k > 0 else "A"
        if (ch, prev_ch, it) in memo:
            ch_len = memo[(ch, prev_ch, it)]
        else:
            new_path = short_robo(ch, get_idx_robo(prev_ch))
            ch_len = expand(new_path, it + 1, limit)
            memo[(ch, prev_ch, it)] = ch_len
        nr += ch_len

    return nr

def shortest(num):
    robo = short_numeric(num)
    robo_nr = 0
    print("Expand", robo)
    robo_nr += expand(robo, 0, 25) # replace with 2 for part_1
    print("Expanded", robo_nr)
    return robo_nr


def short_numeric(num):
    shortest_path = ""
    start = (3, 2)  # A
    for n in num:
        idx = get_idx(n)
        explored = explore_paths_numeric(start, idx, 0, 4)
        shortest_path += "".join([direct_to[e] for e in explored]) + "A"
        start = idx

    return shortest_path


def short_robo(sp, start=(0,2)):
    shortest_path = ""
    for s in sp:
        idx = get_idx_robo(s)
        explored = explore_paths_numeric(start, idx, 0, 2) 
        shortest_path += "".join([direct_to[e] for e in explored]) + "A"
        start = idx

    return shortest_path


moves = []
with open("input/advent21.txt", "r") as file:
    for line in file:
        moves.append(line.strip())

total = 0
for move in moves:
    values = shortest(move)
    print(move, values, "x", get_numeric(move), values * get_numeric(move))
    total += values * get_numeric(move)

print("Total", total)
print("Short robo", "".join([direct_to[e] for e in explore_paths_numeric(get_idx_robo("<"), get_idx_robo("A"), 0, 2)]))
print("Short robo", "".join([direct_to[e] for e in explore_paths_numeric(get_idx_robo("A"), get_idx_robo("<"), 0, 2)]))
