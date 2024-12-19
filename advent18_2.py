def print_grid(grid):
    to_print = ""
    for i in range(N):
        for j in range(M):
            to_print += grid[i][j]
        to_print += "\n"
    print(to_print)

def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M

coordinates = []
with open("input/advent18.txt", "r") as file:
    for line in file:
        a1, a2 = map(int, line.strip().split(","))
        coordinates.append((a1, a2))

N = 71
M = 71
grid = [["." for _ in range(N)] for _ in range(M)]
for coordinate in coordinates[:1024]:
    (j, i) = coordinate
    grid[i][j] = '#'

print_grid(grid)

directions = [(-1, 0),  # up
              (0, 1),  # right
              (1, 0),  # down
              (0, -1)]

start = (0, 0)
end = (M - 1, N - 1)

def explore_paths():

    queue = [(start[0], start[1], 0, 0)]
    did_exit = False
    memo = {}
    while queue:
        i, j, drct, step = queue.pop(0)
        if i == end[0] and j == end[1]:
            did_exit = did_exit or True

        if (i, j, drct) in memo and memo[(i, j, drct)] <= step:  # do not explore if we already explored a shorter path
            continue

        memo[(i, j, drct)] = step

        d = 0
        for direction in directions:
            (di, dj) = direction
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj) and grid[ni][nj] != '#':
                queue.append((ni, nj, d, step + 1))
                d += 1
    print("Exit?", did_exit)
    return did_exit


for (j, i) in coordinates[1024:]:
    grid[i][j] = "#"
    # print_grid(grid)
    has_end = explore_paths()
    if not has_end:
        print("No exit", i, j)
        break
