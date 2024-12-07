from functools import total_ordering

moves = []
right = {"^": ">", ">": "v", "v": "<", "<": "^"}

def dif(dirct):
    if dirct == "^":
        return -1, 0
    elif dirct == ">":
        return 0, 1
    elif dirct == "v":
        return 1, 0
    elif dirct == "<":
        return 0, -1

def pass_guard(moves, k, l, direction):
    i = k
    j = l

    x, y = (0, 0)
    visited = [["" for _ in range(M)] for _ in range(N)]
    passed = []
    while True:
        # move forward if possible
        while 0 <= i + x < N and 0 <= j + y < M and moves[i + x][j + y] != "#":
            if visited[i][j] == direction:
                return True, passed
            visited[i][j] = direction
            passed.append((i, j, direction))
            x, y = dif(direction)
            i += x
            j += y

        # leave the grid
        if i < 1 or i >= N - 1 or j < 1 or j >= M - 1:
            passed.append((i, j, direction))
            return False, passed

        direction = right[direction]
        x, y = dif(direction)


with (open("input.txt", "r") as f):
    for line in f:
        moves.append(list(line.strip()))

    N = len(moves)
    M = len(moves[0])

    guard = None
    for i in range(N):
        for j in range(M):
            if moves[i][j] in "^><v":
                guard = (i, j)

    k = guard[0]
    l = guard[1]
    distinct = 0
    count = [[False for _ in range(M)] for _ in range(N)]
    direction = moves[k][l]

    i = k
    j = l

    _, steps = pass_guard(moves, k, l, direction)
    total = set()

    for step in steps[1:]:
        xo, yo, do  = step
        moves[xo][yo] = '#'
        cycle, _ = pass_guard(moves, k, l, direction)
        if cycle:
            print("Obstacle: ", xo, yo)
            total.add((xo, yo))
        moves[xo][yo] = '.'

print(len(steps), len(total))
