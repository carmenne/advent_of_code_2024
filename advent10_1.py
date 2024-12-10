trail = []

def hike(i, j):
    print("Hike at indexes:", i, j, m, n)
    if i < 0 or i >= m or j < 0 or j >= n:
        return

    position = trail[i][j]

    if position == 9:
        nines.add((i, j))

    if i + 1 < m and trail[i + 1][j] == position + 1:  # DOWN
        print("DOWN", i, j)
        hike(i + 1, j)
    if i - 1 >= 0 and trail[i - 1][j] == position + 1:  # UP
        print("UP", i, j)
        hike(i - 1, j)
    if  j - 1 >= 0 and trail[i][j - 1] == position + 1:
        print("LEFT", i, j)# LEFT
        hike(i, j - 1)
    if j + 1 < n and trail[i][j + 1] == position + 1:
        print("RIGHT", i, j)# RIGHT
        hike(i, j + 1)


with open("input.txt", "r") as file:
    for line in file:
        digits = str(line.strip())
        trail.append([int(d) for d in str(digits)])

    m = len(trail)
    n = len(trail[0])

    routes = set()
    for p in range(m):
        for r in range(n):
            if trail[p][r] == 0:
                routes.add((p, r))

    total = 0
    for x, y in routes:
        nines = set()
        hike(x, y)
        total += len(nines)

    print("Total =", total)
