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