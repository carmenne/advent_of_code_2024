from collections import defaultdict

rocks = []


def print_grid(grid):
    to_print = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            to_print += grid[i][j]
        to_print += "\n"
    print(to_print)


total = 0
count = 0
with open("input_long.txt", "r") as file:
    for line in file:
        rocks.append(list(line.strip()))

DIRECTIONS = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
OPPOSITE = {"E": "W", "W": "E", "N": "S", "S": "N"}

M = len(rocks)
N = len(rocks[0])


def in_bounds(i, j):
    return 0 <= i < M and 0 <= j < N


def tilt_n(rocks):
    for j in range(N):
        pos_i = -1
        for i in range(M):
            if rocks[i][j] in "#":
                pos_i, pos_j = i, j
            if rocks[i][j] == "O":
                pos_i += 1
                rocks[i][j] = "."
                rocks[pos_i][j] = "O"

    return rocks


def tilt_w(rocks):
    for i in range(M):
        pos_j = -1
        for j in range(N):
            if rocks[i][j] in "#":
                pos_i, pos_j = i, j
            if rocks[i][j] == "O":
                pos_j += 1
                rocks[i][j] = "."
                rocks[i][pos_j] = "O"

    return rocks


def tilt_s(rocks):
    for j in range(N):
        pos_i = M
        for i in range(M - 1, -1, -1):
            if rocks[i][j] in "#":
                pos_i, pos_j = i, j
            if rocks[i][j] == "O":
                pos_i -= 1
                rocks[i][j] = "."
                rocks[pos_i][j] = "O"

    return rocks


def tilt_e(rocks):
    for i in range(M):
        pos_j = N
        for j in range(N - 1, -1, -1):
            if rocks[i][j] in "#":
                pos_j = j
            if rocks[i][j] == "O":
                pos_j -= 1
                rocks[i][j] = "."
                rocks[i][pos_j] = "O"

    return rocks


def count_total():
    count_zero = 0
    for i, t in enumerate(rocks):
        count_zero += t.count("O")

    return count_zero


total = 0


def cycle():
    tilt_n(rocks)
    tilt_w(rocks)
    tilt_s(rocks)
    tilt_e(rocks)


def calculate_total():
    total = 0
    for i, t in enumerate(rocks):
        total += (M - i) * t.count("O")
    return total


def to_string(rocks):
    rock = ""
    for i in range(M):
        for j in range(N):
            rock += rocks[i][j]
    return rock


previous = defaultdict(int)


def get_first():
    i = 0
    loads = []
    while True:
        cycle()
        # print_grid(rocks)
        rocks_string = to_string(rocks)
        if rocks_string in previous:
            if previous[rocks_string] == 2:
                return i, loads
            loads.append(calculate_total())

        previous[rocks_string] += 1
        i += 1


first, loads = get_first()

CYCLE = 1000000000
FIRST = first
PERIOD = len(loads)

for i in range(2, PERIOD):
    cycle()
    if i == ((1000000000 - FIRST) % PERIOD):
        print(calculate_total())  # 106390, 99291
