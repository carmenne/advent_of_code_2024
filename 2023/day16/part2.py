from collections import defaultdict

tiles = []
with open("input_long.txt", "r") as file:
    for line in file:
        tiles.append(list(line.strip()))

directions = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
reflections = {
    (">", "\\"): "v", (">", "/"): "^", (">", "|"): "^v", (">", "-"): ">", (">", "."): ">", # rightward
    ("<", "\\"): "^", ("<", "/"): "v", ("<", "|"): "^v", ("<", "-"): "<", ("<", "."): "<", # leftward
    ("^", "\\"): "<", ("^", "/"): ">", ("^", "|"): "^", ("^", "-"): "<>", ("^", "."): "^", # upward
    ("v", "\\"): ">", ("v", "/"): "<", ("v", "|"): "v", ("v", "-"): "<>", ("v", "."): "v", # downward
}

M = len(tiles)
N =  len(tiles[0])

def in_bounds(i, j):
    return 0 <= i < M and 0 <= j < M

def reflect(s1, s2, start):

    energized = {(s1, s2)}
    queue = [(s1, s2,start)]
    memo = defaultdict(int)
    while queue:
        i, j, dir = queue.pop(0)
        refection_moves = reflections[(dir, tiles[i][j])]
        for move in list(refection_moves):
            di, dj = directions[move]
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj) and (ni, nj, move) not in memo:
                energized.add((ni, nj))
                queue.append((ni, nj, move))
                memo[(ni, nj, move)] += 1

    return len(energized)

max_energized = 0
for i in range(M):
    max_energized = max(max_energized, reflect(i, 0, ">"))
    max_energized = max(max_energized, reflect(i, N - 1, "<"))
for j in range(N):
    max_energized = max(max_energized, reflect(0, j, "v"))
    max_energized = max(max_energized, reflect(M - 1, j, "^"))

print(max_energized)