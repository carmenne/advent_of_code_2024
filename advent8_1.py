positions = []


def count(ant1, ant2):
    x1, y1 = ant1
    x2, y2 = ant2
    d1, d2 = abs(x1-x2), abs(y1-y2)

    if x1 >= x2:
        if y1 < y2: #A1A2
            if in_bounds(x1 + d1, y1 - d2):
                antinodes.add((x1 + d1, y1 - d2))
            if in_bounds(x2 - d1, y2 + d2):
                antinodes.add((x2 - d1, y2 + d2))
        if y1 > y2: # A2A1
            if in_bounds(x1 + d1, y1 + d2):
                antinodes.add((x1 + d1, y1 + d2))
            if in_bounds(x2 - d1, y2 - d2):
                antinodes.add((x2 - d1, y2 - d2))
    if x1 < x2:
        if y1 > y2: # vertical A1A2
            if in_bounds(x1 - d1, y1 + d2):
                antinodes.add((x1 - d1, y1 + d2))
            if in_bounds(x2 + d1, y2 - d2):
                antinodes.add((x2 + d1, y2 - d2))
        if y1 <= y2: # vertical A2A1
            if in_bounds(x1 - d1, y1 - d2):
                antinodes.add((x1 - d1, y1 - d2))
            if in_bounds(x2 + d1, y2 + d2):
                antinodes.add((x2 + d1, y2 + d2))


def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M


with (open("input.txt", "r") as file):
    for line in file:
        positions.append(list(line.strip()))

    N = len(positions)
    M = len(positions[0])
    antennas = {}
    antinodes = set()

    for i in range(N):
        for j in range(M):
            if positions[i][j] == ".":
                continue

            # check if we can place antinodes
            curr = positions[i][j]
            if curr in antennas:
                for antenna in antennas[curr]:
                    count(antenna, (i, j))

            # populate antennas
            if curr in antennas:
                antennas[curr].add((i,j))
            else:
                antennas[curr] = {(i,j)}

print(len(antinodes))
