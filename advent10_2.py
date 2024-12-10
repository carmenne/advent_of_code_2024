trail = []

def hike(i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0

    position = trail[i][j]

    result = 1 if position == 9 else 0

    if i + 1 < m and trail[i + 1][j] == position + 1:  # DOWN
        result += hike(i + 1, j)
    if i - 1 >= 0 and trail[i - 1][j] == position + 1:  # UP
        result += hike(i - 1, j)
    if  j - 1 >= 0 and trail[i][j - 1] == position + 1:
        result += hike(i, j - 1)
    if j + 1 < n and trail[i][j + 1] == position + 1:
        result += hike(i, j + 1)

    return result

with open("input.txt", "r") as file:
    for line in file:
        digits = str(line.strip())
        trail.append([-5 if d == "." else int(d) for d in str(digits)])

    m = len(trail)
    n = len(trail[0])

    routes = set()
    nines = set()
    for p in range(m):
        for r in range(n):
            if trail[p][r] == 0:
                routes.add((p, r))

    total = 0
    for x, y in routes:
        total += hike(x, y)

    print("Total =", total)
