pipes = []
with open("input_long.txt", "r") as file:
    for line in file:
        pipes.append(list(line.strip()))


def find_start(area):
    for i in range(M):
        for j in range(N):
            if area[i][j] == "S":
                return i, j


go_next = {
    "|": {(-1, 0), (1, 0)},
    "-": {(0, -1), (0, 1)},
    "F": {(1, 0), (0, 1)},  # S - E
    "7": {(1, 0), (0, -1)},  # S - W
    "L": {(-1, 0), (0, 1)},  # N - E
    "J": {(-1, 0), (0, -1)},  # N - W
}

directions = [(-1, 0),  # up
              (0, 1),  # right
              (1, 0),  # down
              (0, -1)]


def in_bounds(x, y):
    return 0 <= x < M and 0 <= y < N


def move_next(pipe, x, y, from_x, from_y):
    directions = go_next[pipe]
    for dx, dy in directions:
        if (x + dx, y + dy) != (from_x, from_y):
            return dx, dy


path = {}
def find_loop(area, start):
    not_stared = True
    distance = 0
    x, y, from_x, from_y = start[0], start[1] + 1, start[0], start[1]
    direction = (0, 1)
    path[start] = (0, 1)
    while not_stared or area[x][y] != "S":
        not_stared = False
        distance += 1
        path[x, y] = direction

        dx, dy = move_next(area[x][y], x, y, from_x, from_y)
        direction = (dx, dy)
        from_x, from_y = x, y
        x, y = x + dx, y + dy

    return distance

M = len(pipes)
N = len(pipes[0])
start = find_start(pipes)
print(start)
print((find_loop(pipes, start) + 1) // 2)  # 6860


def print_grid(grid):
    to_print = ""
    for i in range(M):
        for j in range(N):
            to_print += grid[i][j]
        to_print += "\n"
    print(to_print)


memo = {}

def fill(start, type):
    queue = [start]
    while queue:
        x, y, from_x, from_y, dx, dy = queue.pop(0)

        if (x, y, from_x, from_y, direction) in memo:
            continue
        memo[(x, y, from_x, from_y, direction)] = True

        if in_bounds(x, y) and (x, y) not in path:
            pipes[x][y] = type

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and (nx, ny) not in set(path):
                    queue.append((nx, ny, x, y, dx, dy))


def in_bounds(x, y):
    return 0 <= x < M and 0 <= y < N


directions = [(-1, 0),  # up
              (0, 1),  # right
              (1, 0),  # down
              (0, -1)]

inside = {
    ("S", 1, 0): [(0, -1)], ("S", 0, 1): [(1, 0)], ("S", -1, 0): [(0, 1)], ("S", 0, -1): [(-1, 0)],
    ("|", 1, 0): [(0, -1)], ("-", 0, 1): [(1, 0)], ("|", -1, 0): [(0, 1)], ("-", 0, -1): [(-1, 0)],
    ("J", 0, 1): [(1, 0), (0, 1)],
    ("7", -1, 0): [(-1, 0), (0, 1)],
    ("L", -1, 0): [(1, 0), (0, -1)],
    ("F", 0, 1): [(-1, 0), (0, -1)]
}
outside = {
    ("S", 1, 0): [(0, 1)], ("S", 0, 1): [(-1, 0)], ("S", -1, 0): [(0, -1)], ("S", 0, -1): [(1, 0)],
    ("|", 1, 0): [(0, 1)], ("-", 0, 1): [(-1, 0)], ("|", -1, 0): [(0, -1)], ("-", 0, -1): [(1, 0)],
    ("7", 0, 1): [(-1, 0), (0, 1)],
    ("J", 1, 0): [(1, 0), (0, 1)],
    ("L", 0, -1): [(1, 0), (0, -1)],
    ("F", -1, 0): [(-1, 0), (0, -1)]
}


def fill_inside(step, direction):
    x, y = step
    dx, dy = direction
    insides = [] if (pipes[x][y], dx, dy) not in inside else inside[(pipes[x][y], dx, dy)]
    for idx, idy in insides:
        ix, iy = x + idx, y + idy
        if in_bounds(ix, iy) and (ix, iy) not in path:
            fill((ix, iy, ix, iy, dx, dy), "I")


def fill_outside(step, direction):
    x, y = step
    dx, dy = direction
    outsides = [] if (pipes[x][y], dx, dy) not in outside else outside[(pipes[x][y], dx, dy)]
    for odx, ody in outsides:
        ox, oy = x + odx, y + ody
        if in_bounds(ox, oy) and (ox, oy) not in path:
            fill((ox, oy, ox, oy, dx, dy), "O")


for step, direction in path.items():
    i, j = step

    fill_inside(step, direction)
    fill_outside(step, direction)

inside = 0
outside = 0
total = 0

print(inside, outside, len(path), total, inside + outside + len(path)) #343 5537 13720 19600 19600
