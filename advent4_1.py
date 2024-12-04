
def dfs(chars, m, n, i, j, word, visited, i_prev, j_prev, direction):

    if i >= m or j >= n or i < 0 or j < 0:
        return 0

    if visited[i][j]:
        return 0

    if direction == "UP_LEFT" and not (i == i_prev - 1 and j  == j_prev - 1):
            return 0
    elif direction == "UP" and not (i == i_prev - 1 and j == j_prev):
        return 0
    elif direction == "UP_RIGHT" and not (i == i_prev - 1 and j == j_prev + 1):
        return 0
    elif direction == "LEFT" and not (i == i_prev and j == j_prev - 1):
        return 0
    elif direction == "RIGHT" and not(i == i_prev and j == j_prev + 1):
        return 0
    elif direction == "BOTTOM_LEFT" and not(i == i_prev + 1 and j == j_prev - 1):
        return 0
    elif direction == "BOTTOM" and not (i == i_prev + 1 and j == j_prev):
        return 0
    elif direction == "BOTTOM_RIGHT" and not (i == i_prev + 1 and j == j_prev + 1):
        return 0

    letter = chars[i][j]
    word += letter
    visited[i][j] = True

    if letter not in "XMAS":
        return 0

    if letter == "M" and word != "XM":
        return 0

    elif letter == "A" and word != "XMA":
        return 0
    elif letter == "S" and word != "XMAS":
        return 0

    if len(word) > 4:
        return 0

    xmas_count = 1 if word == "XMAS" else 0

    return xmas_count + \
            + dfs(chars, m, n, i - 1, j - 1, word, visited, i, j, "UP_LEFT" if direction == "" else direction) \
            + dfs(chars, m, n, i - 1, j, word, visited, i, j, "UP" if direction == "" else direction) \
            + dfs(chars, m, n, i - 1, j + 1, word, visited, i, j, "UP_RIGHT" if direction == "" else direction) \
            + dfs(chars, m, n, i, j - 1, word, visited, i, j, "LEFT" if direction == "" else direction) \
            + dfs(chars, m, n, i, j + 1, word, visited, i, j, "RIGHT" if direction == "" else direction) \
            + dfs(chars, m, n, i + 1, j - 1, word, visited, i, j, "BOTTOM_LEFT" if direction == "" else direction) \
            + dfs(chars, m, n, i + 1, j, word, visited, i, j, "BOTTOM" if direction == "" else direction) \
            + dfs(chars, m, n, i + 1, j + 1, word, visited, i, j, "BOTTOM_RIGHT" if direction == "" else direction)


letters = []
with open("input.txt", "r") as file:
    for line in file:
        letters.append(list(line.replace("\n", "")))

    xmas = 0
    row = len(letters)
    column = len(letters[0])
    for x in range(row):
        for y in range(column):
            if letters[x][y] == "X":
                xmas += dfs(letters, row, column, x, y, "", [[False for _ in range(column)] for _ in range(row)], x, y, "")

    print(xmas)
