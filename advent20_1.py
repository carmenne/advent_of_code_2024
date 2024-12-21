def print_grid(grid):
    to_print = ""
    for i in range(N):
        for j in range(M):
            to_print += grid[i][j]
        to_print += "\n"
    print(to_print)


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M


maze = []
with open("input/advent20.txt", "r") as file:
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

directions = [(-1, 0),  # up
              (0, 1),  # right
              (1, 0),  # down
              (0, -1)]

visited = {}


def explore_paths():
    steps = 0
    i, j = start[0], start[1]
    while not (i == end[0] and j == end[1]):
        visited[(i, j)] = steps
        steps += 1
        for direction in directions:
            (di, dj) = direction
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj) and maze[ni][nj] != '#' and (ni, nj) not in visited:
                i, j = ni, nj
                break
    return steps


shortest_path = explore_paths()
visited[end] = shortest_path
print(shortest_path)

difs = 0
sec = 2
for vis in visited:
    x, y = vis
    for direction in directions:
        (dx, dy) = direction
        nx, ny = x + sec * dx, y + sec * dy
        if in_bounds(nx, ny) and (nx, ny) in visited:
            dif = visited[(x, y)] - (visited[(nx, ny)] + sec)
            if dif >= 100:
                difs += 1

print(difs) # 1321
