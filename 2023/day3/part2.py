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

def discover_part(x, y):
    left = y
    while in_bounds(x, left) and grid[x][left] in "0123456789":
        left -= 1
    right = y
    while in_bounds(x, right) and grid[x][right] in "0123456789":
        right += 1

    number = ""
    for j in range(left + 1, right):
        number += grid[x][j]

    return int(number)


def discover_gears(i, j):
    gears = set()
    for di,dj in directions:
        if in_bounds(i + di, j + dj) and grid[i+di][j+dj] in "0123456789":
            gears.add(discover_part(i + di, j + dj))

    return gears

total = 0
for i in range(M):
    number = ""
    for j in range(N):
        if in_bounds(i, j) and grid[i][j] == "*":
            gears = discover_gears(i, j)
            if len(gears) == 2:
                prod = 1
                for gear in gears:
                    prod *= gear
                total += prod

print(total)  # 76504829