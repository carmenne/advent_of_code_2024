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


def tilt(rocks, direction):
    for i in range(M):
        for j in range(N):
            if rocks[i][j] == "O":
                di, dj = DIRECTIONS[direction]
                new_i, new_j = i + di, j + dj
                while in_bounds(new_i, new_j) and rocks[new_i][new_j] == ".":
                    rocks[new_i][new_j] = "O"
                    o_di, o_dj = DIRECTIONS[OPPOSITE[direction]]
                    prev_i, prev_j = new_i + o_di, new_j + o_dj
                    rocks[prev_i][prev_j] = "."
                    new_i, new_j = new_i + di, new_j + dj
    return rocks


def tilt_s(rocks, direction):
    for i in range(M - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if rocks[i][j] == "O":
                di, dj = DIRECTIONS[direction]
                new_i, new_j = i + di, j + dj
                while in_bounds(new_i, new_j) and rocks[new_i][new_j] == ".":
                    rocks[new_i][new_j] = "O"
                    o_di, o_dj = DIRECTIONS[OPPOSITE[direction]]
                    prev_i, prev_j = new_i + o_di, new_j + o_dj
                    rocks[prev_i][prev_j] = "."
                    new_i, new_j = new_i + di, new_j + dj
    return rocks


def count_total():
    count_zero = 0
    for i, t in enumerate(rocks):
        count_zero += t.count("O")

    return count_zero


total = 0


def cycle():
    tilt(rocks, "N")
    tilt(rocks, "W")
    tilt_s(rocks, "S")
    tilt_s(rocks, "E")


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
        rocks_string = to_string(rocks)
        if rocks_string in previous:
            if previous[rocks_string] == 2:
                return i, loads
            loads.append(calculate_total())

        previous[rocks_string] += 1
        i += 1


first, loads = get_first()
# print("Loads", len(loads), first, first - len(loads), loads)

CYCLE = 1000000000
FIRST = first
PERIOD = len(loads)

for i in range(2, PERIOD):
    cycle()
    if i == ((1000000000 - FIRST) % PERIOD):
        print(calculate_total()) # 106390, 99291
