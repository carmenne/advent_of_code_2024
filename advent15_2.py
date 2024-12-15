from time import sleep

warehouse = []
moves_input = []
direction = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
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
    to_print = ""
    for row in grid:
        for col in row:
            if col == '@':
                to_print += "🎅"
            elif col == "#":
                to_print += "🧱"
            elif col == ".":
                to_print += "⬛"
            elif col == "[":
                to_print += "🎄"
            else:
                to_print += "🎄"

        to_print += "\n"
    print(to_print)
    sleep(0.1)

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

    if my == 0: # up and down
        if wide[new_x][new_y] == "]" and wide[new_x][new_y - 1] == "[":
            return can_move_box((new_x, new_y), move) and can_move_box((new_x, new_y - 1), move)
        elif wide[new_x][new_y] == "[" and wide[new_x][new_y + 1] == "]":
            return can_move_box((new_x, new_y), move) and can_move_box((new_x, new_y + 1), move)
    else:
        return can_move_box((new_x, new_y), move)
    return False

def move_it(c, d, a, b):
    wide[c][d] = wide[a][b]
    wide[a][b] = "."


def move_box(pos, move):
    x, y = pos
    mx, my = move
    new_x, new_y = x + mx, y + my

    if wide[new_x][new_y] == "#":
        return

    if my == 0:
        if wide[new_x][new_y] == "]" and wide[new_x][new_y - 1] == "[":
            move_box((new_x, new_y), move)
            move_box((new_x, new_y - 1), move)
        elif wide[new_x][new_y] == "[" and wide[new_x][new_y + 1] == "]":
            move_box((new_x, new_y), move)
            move_box((new_x, new_y + 1), move)
    else:
        if wide[new_x][new_y] in "][":
            move_box((new_x, new_y), move)

    move_it(new_x, new_y, x, y)

for mx, my in moves:
    x, y = robo
    if wide[x + mx][y + my] == "#":
        continue
    elif wide[x + mx][y + my] == ".":
        wide[x][y] = "."
        wide[x + mx][y + my] = "@"
        robo = (x + mx, y + my)
    else:
        can_move = can_move_box((x, y), (mx, my))
        if can_move:
            new_moves = {}
            move_box((x, y), (mx, my))
            robo = (x + mx, y + my)
    print_grid(wide)

boxes = 0
for i in range(M):
    for j in range(2*N):
        if wide[i][j] in '[':
            boxes += 100 * i + j

print(boxes) # 1509724
