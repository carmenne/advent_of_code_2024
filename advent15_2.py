warehouse = []
moves_input = []
direction = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
reverse = {(0, -1): "<", (-1, 0): "^", (0, 1): ">", (1, 0): "v"}
with open("input/advent15.txt", "r") as file:
    for l in file:
        if l == "\n": continue
        line = l.strip()
        if line[0] == "#":
            warehouse.append(list(line))
        else:
            moves_input += list(line)

moves = [direction[m] for m in moves_input]  # <^^>>>vv<v>>v<<
M = len(warehouse)
N = len(warehouse[0])


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")


def in_bounds(i, j):
    return 0 <= i < M and 0 <= j < 2 * N


wide = [["+" for _ in range(2 * N)] for _ in range(M)]

for i in range(M):
    for j in range(N):
        if warehouse[i][j] == "#":
            wide[i][2 * j] = "#"
            wide[i][2 * j + 1] = "#"
        elif warehouse[i][j] == "O":
            wide[i][2 * j] = "["
            wide[i][2 * j + 1] = "]"
        elif warehouse[i][j] == ".":
            wide[i][2 * j] = "."
            wide[i][2 * j + 1] = "."
        elif warehouse[i][j] == "@":
            wide[i][2 * j] = "@"
            wide[i][2 * j + 1] = "."

# find robo
robo = None
for i in range(M):
    for j in range(2 * N):
        if wide[i][j] == "@":
            robo = (i, j)
            break


# move robo
def can_move_box(pos, move):
    x, y = pos
    mx, my = move
    new_x, new_y = x + mx, y + my

    if wide[new_x][new_y] == "#":
        return False
    if wide[new_x][new_y] == ".":
        return True

    if wide[new_x][new_y] == "]" and wide[new_x][new_y - 1] == "[":
        return can_move_box((new_x, new_y), move) and can_move_box((new_x, new_y - 1), move)
    elif wide[new_x][new_y] == "[" and wide[new_x][new_y + 1] == "]":
        return can_move_box((new_x, new_y), move) and can_move_box((new_x, new_y + 1), move)

    return False

def move_box(pos, move, new_moves):
    x, y = pos
    mx, my = move
    new_x, new_y = x + mx, y + my

    if wide[new_x][new_y] == "]" and wide[new_x][new_y - 1] == "[":
        move_box((new_x, new_y), move, new_moves)
        move_box((new_x, new_y - 1), move, new_moves)
    elif wide[new_x][new_y] == "[" and wide[new_x][new_y + 1] == "]":
        move_box((new_x, new_y), move, new_moves)
        move_box((new_x, new_y + 1), move, new_moves)

    if in_bounds(new_x, new_y):
        new_moves[(x, y)] = (new_x, new_y)  # I am such an idiot

for mx, my in moves:
    x, y = robo
    if not in_bounds(x + mx, y + my) or wide[x + mx][y + my] == "#":
        # print("not moved #", reverse[(mx, my)])
        continue
    elif wide[x + mx][y + my] == ".":
        wide[x][y] = "."
        wide[x + mx][y + my] = "@"
        robo = (x + mx, y + my)
    elif reverse[(mx, my)] == '<' or reverse[(mx, my)] == '>':  # let's move some boxes
        k, l = x + mx, y + my
        while in_bounds(k, l) and wide[k][l] in '[]':
            k += mx
            l += my

        moved = False
        if in_bounds(k, l) and wide[k][l] == '.':  # we can actually move
            while (k, l) != (x, y):
                moved = True
                wide[k][l] = wide[k - mx][l - my]
                if wide[k][l] == "@":
                    robo = (k, l)
                k -= mx
                l -= my

            if moved:
                wide[k][l] = "."
    else:  # up and down: []

        can_move = can_move_box((x, y), (mx, my))
        if can_move:
            new_moves = {}
            move_box((x, y), (mx, my), new_moves)
            to_move = sorted(new_moves) if mx == -1 else reversed(sorted(new_moves))
            for fr in to_move:
                fr_x, fr_y = fr
                to_x, to_y = new_moves[fr]
                wide[to_x][to_y] = wide[fr_x][fr_y]
                wide[fr_x][fr_y] = "."
            robo = (x + mx, y + my)

print_grid(wide)

boxes = 0
for i in range(M):
    for j in range(2*N):
        if wide[i][j] in '[':
            boxes += 100 * i + j

print(boxes)
