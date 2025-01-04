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

DIRECTIONS = {"E": (0, -1), "W": (0, 1), "N": (-1, 0), "S": (1, 0)}
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

total = 0
tilted = tilt(rocks, "N")

for i, t in enumerate(tilted):
    total += (M - i) * t.count("O")

print(total) # 106186
