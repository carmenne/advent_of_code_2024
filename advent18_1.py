import heapq

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

N = 7
M = 7
grid = [["." for _ in range(N)] for _ in range(M)]
memo = {}
for coordinate in coordinates[:12]:
    (j, i) = coordinate
    grid[i][j] = '#'

print_grid(grid)
start = (0, 0)
end = (M - 1, N - 1)

queue = [(start[0], start[1], 0, 0)]
directions = [(-1, 0),  # up
             (0, 1),  # right
             (1, 0),  # down
             (0, -1)]

min_steps = float('inf')
steps = set()
while queue:
    i, j, drct, step = queue.pop(0)
    steps.add((i,j))
    print("Explore", i, j, min_steps)

    if i == end[0] and j == end[1]:
        if min_steps > step:
            steps = set()
        min_steps = min(min_steps, step)

    if (i, j, drct) in memo and memo[(i, j, drct)] <= step: # do not explore if we already explored a shorter path
        continue

    memo[(i, j, drct)] = step

    d = 0
    for direction in directions:
        (di, dj) = direction
        ni, nj = i + di, j + dj
        if in_bounds(ni, nj) and grid[ni][nj] != '#':
            queue.append((ni, nj, d, step + 1))
            d += 1

print(min_steps, steps)

for s in steps:
    si, sj = s
    grid[si][sj] = '0'

print_grid(grid)
