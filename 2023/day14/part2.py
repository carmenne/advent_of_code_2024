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


CYCLE = 1000000000
FIRST = 122
PERIOD = 22
for i in range(FIRST):
    cycle()
    print(i, calculate_total())

for i in range(1, PERIOD + 1):
    cycle()
    if i == ((1000000000 - 122) % 22):
        print(calculate_total())
