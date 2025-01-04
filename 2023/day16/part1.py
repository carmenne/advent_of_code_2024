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

energized = {(0,0)}
queue = [(0, 0, ">")]
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

print(len(energized)) # 6514