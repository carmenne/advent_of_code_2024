from collections import defaultdict

plants = []
with open("input.txt", "r") as file:
    plants += [list(line.strip()) for line in file]

m = len(plants)
n = len(plants[0])

dist = {(-1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (1, 0, "U")}
new_dist = {(0, -1, "L"), (1, 0, "U")}


def in_bounds(i, j):
    return 0 <= i < m and 0 <= j < n


def area(i, j, plant):
    if i >= m or j >= n or i < 0 or j < 0:
        return 0

    if visited[i][j]:
        return 0

    visited[i][j] = True
    count = 1

    for dx, dy, d in dist:
        nx, ny = i + dx, j + dy
        if not in_bounds(nx, ny) or plants[i][j] != plants[nx][ny]:
            directions[(i, j)].add(d)
        if in_bounds(nx, ny) and plants[nx][ny] == plant:
            count += area(nx, ny, plant)

    return count


def none(pot, neighbours):
    x, y, d = pot
    for dx, dy, _ in dist:
        if (x + dx, y + dy, d) in neighbours:
            return False
    return True


def count_distinct():
    count = 0
    for k in range(0, m):
        for l in range(0, n):
            if (k, l) in directions:
                neighbours = {
                    (k + dx, l + dy, nd)
                    for dx, dy, _ in new_dist
                    if (k + dx, l + dy) in directions
                    for nd in directions[k + dx, l + dy]
                }

                count += sum(1 for d in directions[(k, l)] if none((k, l, d), neighbours))
    return count


visited = [[False for _ in range(m)] for _ in range(n)]
total = 0
for i in range(m):
    for j in range(n):
        directions = defaultdict(set)
        region_count = area(i, j, plants[i][j])
        if region_count > 0:
            distinct = count_distinct()
            total += region_count * distinct

print("Total", total)
