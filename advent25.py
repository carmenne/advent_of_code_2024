locks_and_keys = []
tmp = []
with open("input/advent25.txt") as file:
    for line in file:
        if line == "\n":
            locks_and_keys.append(tmp)
            tmp = []
        else:
            tmp.append(line.strip())

N = 5
M = 7
print(M, N)

def parse_lock(lock_and_key):
    grid = [None] * N
    for i in range(M):
        for j in range(N):
            if lock_and_key[i][j] == ".":
                if grid[j] is None:
                    grid[j] = i - 1
    return grid


def parse_key(lock_and_key):
    grid = [None] * N
    for i in range(M - 1, -1, -1):
        for j in range(N):
            if lock_and_key[i][j] == ".":
                if grid[j] is None:
                    grid[j] = M - i - 2
    return grid


locks = []
keys = []
for lock_and_key in locks_and_keys:
    if "." not in lock_and_key[0]:  # lock
        locks.append(parse_lock(lock_and_key))
    else:
        keys.append(parse_key(lock_and_key))

def is_match(key, lock):
    for j in range(N):
        if key[j] + lock[j] > N:
            return False

    return True

matching = 0
for key in keys:
    for lock in locks:
        matching += is_match(key, lock)

print("Matching", matching)
