grid = []
with open("input.txt", "r") as file:
    for line in file:
        line_strip = line.strip()
        grid.append(list(line_strip))


def in_bounds(x, y):
    return 0 <= x < M and 0 <= y < N

M = len(grid)
N = len(grid[0])

directions = {(0, 1), (-1, -1), (0, 0), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, -1)}

def is_part(number, i, j):
    for k in range(0, len(number)):
        for di, dj in directions:
            if in_bounds(i + di, j - k - 1 + dj):
                x = grid[i + di][j - k - 1 + dj]
                if x not in "0123456789.":
                    return True

    return False


parts = []
for i in range(M):
    number = ""
    for j in range(N):
        if in_bounds(i, j) and grid[i][j] in "0123456789":
            number += grid[i][j]
        if (in_bounds(i, j) and grid[i][j] not in "0123456789") or (grid[i][j] in "0123456789" and j == N - 1):
            if number != "":
                if is_part(number, i, j):
                    parts.append(int(number))
                number = ""

print(sum(parts))  # 525119
