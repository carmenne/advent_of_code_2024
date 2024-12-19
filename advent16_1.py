import sys

maze = []
sys.setrecursionlimit(10000)


with open("input/advent16.txt", "r") as file:
    for line in file:
        maze.append(list(line.strip()))

M = len(maze)
N = len(maze[0])
# find robo
start = None
end = None
for i in range(M):
    for j in range(N):
        if maze[i][j] == "S":
            start = (i, j)
        elif maze[i][j] == "E":
            end = (i, j)

print(start, end)

memo = {}

direction = [(-1, 0),  # up
             (0, 1),  # right
             (1, 0),  # down
             (0, -1)]  # left


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M

min_cost = float('inf')
queue = [(start[0], start[1], 1, 0)]
while queue:
    i, j, curr, cost = queue.pop(0)
    if maze[i][j] == "#":
        continue
    if maze[i][j] == "E":
        min_cost = min(cost, min_cost)

    if (i, j, curr) in memo and memo[(i, j, curr)] <= cost:
        continue

    memo[(i, j, curr)] = cost
    # Move forward
    ci, cj = direction[curr]

    queue.append((i + ci, j + cj, curr, cost + 1))
    # Turn left
    queue.append((i, j, (curr - 1) % 4, cost + 1000))
    # Turn right
    queue.append((i, j, (curr + 1) % 4, cost + 1000))

print(min_cost)
