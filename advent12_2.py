plants = []
with open("input.txt", "r") as file:
    plants += [list(line.strip()) for line in file]

m = len(plants)
n = len(plants[0])

dist = {(-1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (1, 0, "U")}
reverse = {(-1, 0): "U", (0, -1): "L", (0, 1): "R", (1, 0): "D"}
new_dist = {(0, -1, "L"), (1, 0, "U")}

def in_bounds(i, j):
    return 0 <= i < m and 0 <= j < n


def area(i, j, visited, plant, directions):
    if i >= m or j >= n or i < 0 or j < 0:
        return 0, 0

    if visited[i][j]:
        return 0, 0

    for dx, dy, d in dist:
        if not in_bounds(i + dx, j + dy):
            if (i, j) in directions:
                directions[i, j].add(reverse[(dx, dy)])
            else:
                directions[i, j] = {reverse[(dx, dy)]}

        elif plants[i][j] != plants[i + dx][j + dy]:
            if (i, j) in directions:
                directions[i, j].add(reverse[(dx, dy)])
            else:
                directions[i, j] = {reverse[(dx, dy)]}

    visited[i][j] = True
    count = 1
    fences = 0

    for dx, dy, d in dist:
        x = i + dx
        y = j + dy
        if not in_bounds(x, y) or plants[x][y] != plant:
            fences += 1

        else:
            sub_count, sub_fence = area(x, y, visited, plant, directions)
            count += sub_count
            fences += sub_fence

    return count, fences


visited = [[False for _ in range(m)] for _ in range(n)]
total = 0


def none(pot, neighbours):
    x, y, d = pot
    for dx, dy, _ in dist:
        if (x + dx, y + dy, d) in neighbours:
            return False
    return True


def count_distinct():

    new_set = set()

    for k in range(0, m):
        for l in range(0, n):
            if (k, l) in directions:

                neighbours = set()
                for dx, dy, _ in new_dist:
                    if (k + dx, l + dy) in directions:
                        for nd in directions[k + dx, l + dy]:
                            neighbours.add((k + dx, l + dy, nd))
                            # check
                for d in directions[(k, l)]:
                    if none((k, l, d), neighbours):
                        new_set.add((k, l, d))

    return len(new_set)


for i in range(m):
    for j in range(n):
        directions = {}
        region_count, region_fence = area(i, j, visited, plants[i][j], directions)
        if region_count > 0:
            distinct = count_distinct()
            total += region_count * distinct

print("Total", total)
