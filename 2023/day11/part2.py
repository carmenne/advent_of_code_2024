import itertools

FACTOR = 1_000_000

galaxies = []
rows_expanded = set()
with open("input_long.txt", "r") as file:
    i = 0
    for line in file:
        galaxies.append(list(line.strip()))
        if "#" not in line:
            print(line)
            rows_expanded.add(i)
        i += 1

M = len(galaxies)
N = len(galaxies[0])

def print_grid(grid, M, N):
    to_print = ""
    for i in range(M):
        for j in range(N):
            to_print += str(grid[i][j])
        to_print += "\n"
    print(to_print)


def reverse(galaxies):
    return [[galaxies[i][j] for i in range(len(galaxies))] for j in range(len(galaxies[0]))]
reversed_galaxies = reverse(galaxies)

columns_expanded = set()
i = 0
for row in reversed_galaxies:
    if "#" not in row:
        columns_expanded.add(i)
    i += 1

def in_bounds(x, y, Mlen, Nlen):
    return 0 <= x < Mlen and 0 <= y < Nlen

def shortest_path(start, end):
    s0, s1 = start[0], start[1]
    e0, e1 = end[0], end[1]

    return (abs(s0-e0) + abs(s1-e1) +
            abs(expanded_rows[s0][s1] - expanded_rows[e0][e1]) +
            abs(expanded_columns[s0][s1] - expanded_columns[e0][e1]))

expanded_rows = [[0 for i in range(N)] for j in range(M)]
rows = 0
columns = 0
print(rows_expanded)
print(columns_expanded)
for i in range(M):
    if i in rows_expanded:
        rows += FACTOR - 1
        print(rows)
    for j in range(N):
        expanded_rows[i][j] = rows

expanded_columns = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    columns = 0
    for j in range(N):
        if j in columns_expanded:
            columns += FACTOR - 1
        expanded_columns[i][j] = columns

print_grid(expanded_rows, M, N)
print_grid(expanded_columns, M, N)

galaxy_nodes = set()
for i in range(M):
    for j in range(N):
        if galaxies[i][j] == "#":
            galaxy_nodes.add((i, j))

total = 0
count = 0
combinations = itertools.combinations(galaxy_nodes, 2)
for combination in combinations:

    path = shortest_path(combination[0], combination[1])
    count += 1
    total += path

print(total) #298932923702
