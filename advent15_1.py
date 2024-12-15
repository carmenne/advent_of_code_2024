warehouse = []
moves_input = []
direction = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
reverse = {(0, -1): "<", (-1, 0): "^", (0, 1):  ">",(1, 0):  "v"}
with open("input/advent15.txt", "r") as file:
    for l in file:
        if l == "\n": continue
        line = l.strip()
        if line[0] == "#":
            warehouse.append(list(line))
        else:
            moves_input += list(line)

moves = [ direction[m] for m in moves_input] # <^^>>>vv<v>>v<<
M = len(warehouse)
N = len(warehouse[0])

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end = "")
        print("")

def in_bounds(i, j):
    return 0 <= i < M and 0 <= j < N
# find robo
robo = None
for i in range(M):
    for j in range(N):
        if warehouse[i][j] == "@":
            robo = (i, j)
            break

# move robo
for mx, my in moves:
    x, y = robo
    if not in_bounds(x + mx, y + my) or warehouse[x + mx][y + my] == "#":
        # print("not moved #", reverse[(mx, my)])
        continue
    elif warehouse[x + mx][y + my] == ".":
        warehouse[x][y] = "."
        warehouse[x + mx][y + my] = "@"
        robo = (x + mx, y + my)
        print("Robo moved to", robo, "after", reverse[(mx, my)])
    else: # let's move some boxes
        k, l = x + mx, y + my
        while in_bounds(k, l) and warehouse[k][l] == 'O':
            k += mx
            l += my

        moved = False
        if in_bounds(k, l) and warehouse[k][l] == '.': # we can actually move
            while (k, l) != (x,y):
                moved = True
                warehouse[k][l] = warehouse[k-mx][l-my]
                if warehouse[k][l] == "@":
                    robo = (k, l)
                    print("Robo moved to", robo, "after", reverse[(mx, my)])
                k -= mx
                l -= my

            if moved:
                warehouse[k][l] = "."

print_grid(warehouse)
boxes = 0
for i in range(M):
    for j in range(N):
        if warehouse[i][j] == 'O':
            boxes += 100 * i + j

print(boxes) # 1475249
