pattern = []


def two_columns_equal(pattern, j1, j2, smudge):
    for i in range(len(pattern)):
        if pattern[i][j1] != pattern[i][j2]:
            smudge += 1
    return smudge


def two_rows_equal(pattern, i1, i2, smudge):
    for j in range(len(pattern[0])):
        if pattern[i1][j] != pattern[i2][j]:
            smudge += 1
    return smudge


def vertical_mirror(pattern):

    N = len(pattern[0])
    for column in range(0, N):
        l, r = column, column + 1
        cols = l
        s = 0
        while l >= 0 and r < N and (s:= two_columns_equal(pattern, l, r, s)) <= 1:
            if (l == 0 or r == N - 1) and s == 1:
                return cols + 1
            l -= 1
            r += 1

    return 0


def horizontal_mirror(pattern):
    M = len(pattern)
    for row in range(0, M):
        t, d = row, row + 1
        rolls = t
        s = 0
        while t >= 0 and d < M and (s:= two_rows_equal(pattern, t, d, s)) <= 1:
            if (t == 0 or d == M - 1) and s == 1:
                return rolls + 1
            t -= 1
            d += 1

    return 0


def find_mirrors(pattern):
    columns = vertical_mirror(pattern)
    rows = horizontal_mirror(pattern)
    return rows, columns


total = 0
count = 0
with open("input_long.txt", "r") as file:
    for line in file:
        if line.strip() != "":
            pattern.append(list(line.strip()))

        elif line.strip() == "":
            r, c = find_mirrors(pattern)
            print(count, r, c)
            count += 1
            total += 100 * r + c
            pattern = []


print(total)
print(count)