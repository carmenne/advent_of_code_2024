import time


def print_grid(grid):
    for row in grid:
        for j in range(N):
            if row[j] > 0:
                print(row[j], end="")
            else:
                print(".", end="")
        print("")

robots = []
with open("input.txt", "r") as file:
    for line in file:
        p, v = line.strip().split()
        ps = p.replace("p=", "").split(",")
        vs = v.replace("v=", "").split(",")
        robots.append(((int(ps[0]), int(ps[1])), (int(vs[0]), int(vs[1]))))

M = 103
N = 101
positions = [[0 for _ in  range(N)] for _ in range (M)]

def sum3(k, l, new_positions):
    sum3x3 = 0
    for x in range(k, k + 3):
        for y in range(l, l + 3):
            sum3x3 += new_positions[x][y]
    return sum3x3

# moves
def search_egg(s):
    new_positions = [[0 for _ in  range(N)] for _ in range (M)]
    for robot in robots:
        p, v = robot
        py, px = p
        new_positions[px][py] += 1

    for a in range(M - 3):
        for b in range(N - 3):
            if sum3(a, b, new_positions) == 9:
                print("Seconds", s + 1)
                print_grid(new_positions)
                break


start_time = time.time()
for s in range(10000):
    for k in range(len(robots)):
        (px, py), (vx, vy) = robots[k]
        new_px = ( px + vx if px + vx > 0 else (N - abs(px + vx))) % N
        new_py = (py + vy if py + vy > 0 else (M - abs(py + vy)) ) % M
        robots[k] = ((new_px, new_py), (vx, vy))
    search_egg(s)
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime:.6f} seconds")
