from filecmp import dircmp

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

with (open("advent/input.txt", "r") as f):
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

    x, y = (0, 0)
    while True:
        # move forward if possible
        while 0 <= i + x < N and 0 <= j + y < M and moves[i + x][j + y] != "#":
            distinct += (1 if not count[i][j] else 0)
            count[i][j] = True
            x, y = dif(direction)
            i += x
            j += y

        # leave the grid
        if i < 1 or i >= N - 1 or j < 1 or j >= M - 1:
            distinct += 1
            print(i, j)
            break

        direction = right[direction]
        x, y = dif(direction)

print(distinct)
