import heapq

def print_grid(grid):
    to_print = ""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            to_print += str(grid[i][j])
        to_print += "\n"
    print(to_print)


crucibles = []
with open("input_long.txt", "r") as file:
    for line in file:
        crucibles.append([int(el) for el in list(line.strip())])
directions = [(-1, 0),  (0, 1),(1, 0),  (0, -1)]
directions_display = ["^", ">", "v", "<"]
M = len(crucibles)
N = len(crucibles[0])
print(M, N)

def in_bounds(x, y):
    return 0 <= x < M and 0 <= y < N


def calculate_cost():

    prev = {}
    end = (M - 1, N - 1)
    path = []
    heapq.heapify(path)
    heapq.heappush(path, (0, (0, 0, 1, 0)))
    heapq.heappush(path, (0, (0, 0, 2, 0)))
    memo = {}
    min_cost = float('inf')
    final_node = None

    def go_next(cost, item, fwd, direction):
        di, dj = directions[direction]
        ni, nj = i + di, j + dj
        if in_bounds(ni, nj):
            new_item = (ni, nj, direction, fwd)
            if new_item not in memo or memo[new_item] > cost + crucibles[ni][nj]:
                prev[new_item] = item
                heapq.heappush(path, (cost + crucibles[ni][nj], new_item))

    while path:

        cost, item = heapq.heappop(path)
        if item in memo and memo[item] <= cost:
            continue

        memo[item] = cost

        i, j, direction, fwd = item
        memo[item] = cost

        if (i, j) == end:
            if cost < min_cost:
                min_cost = cost
                final_node = item
            return min_cost, final_node, prev


        if fwd < 10:  # move in the same direction if less than 3
            i, j, direction, fwd = item
            go_next(cost, item, fwd + 1, direction)

        if fwd >= 4:
            for k in (-1, 1):
                new_direction = (direction + k) % 4
                go_next(cost, item, 1, new_direction)

    return min_cost, final_node, prev

min_cost_total, last, prev = calculate_cost()

node = last
while node:
    i, j, direction, _ = node
    crucibles[i][j] = directions_display[direction]
    node = prev.get(node, None)

print_grid(crucibles)

print(min_cost_total) # 1416
