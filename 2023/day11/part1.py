import itertools

galaxies = []
with open("input_long.txt", "r") as file:
    for line in file:
        if "#" not in line:
            galaxies.append(list(line.strip()))
            galaxies.append(list(line.strip()))
        else:
            galaxies.append(list(line.strip()))

M = len(galaxies)
N = len(galaxies[0])


def print_grid(grid, M, N):
    to_print = ""
    for i in range(M):
        for j in range(N):
            to_print += grid[i][j]
        to_print += "\n"
    print(to_print)


def reverse(galaxies):
    return [[galaxies[i][j] for i in range(len(galaxies))] for j in range(len(galaxies[0]))]


reversed_galaxies = reverse(galaxies)

length = len(reversed_galaxies)
expanded_reversed = []
for row in reversed_galaxies:
    if "#" not in row:
        expanded_reversed.append(row)
        expanded_reversed.append(row)
    else:
        expanded_reversed.append(row)

expanded = reverse(expanded_reversed)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_bounds(x, y, Mlen, Nlen):
    return 0 <= x < Mlen and 0 <= y < Nlen

def shortest_path(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

Mlen = len(expanded)
Nlen = len(expanded[0])
print_grid(expanded, Mlen, Nlen)

galaxy_nodes = set()
for i in range(Mlen):
    for j in range(Nlen):
        if expanded[i][j] == "#":
            galaxy_nodes.add((i, j))

total = 0
count = 0
combinations = itertools.combinations(galaxy_nodes, 2)
for combination in combinations:

    path = shortest_path(combination[0], combination[1])
    count += 1
    total += path

print(total) #9521550
