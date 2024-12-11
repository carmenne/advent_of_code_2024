def dfs(chars, m, n, i, j, word, i_prev, j_prev, direction):
    if i >= m or j >= n or i < 0 or j < 0:
        return 0

    for dx, dy, dirct in dist:
        if direction == dirct and not (i_prev + dx == i and j_prev + dy == j):
            return 0

    letter = chars[i][j]
    word += letter

    if letter not in "XMAS" or len(word) > 4:
        return 0
    expected_words = {"M":"XM", "A":"XMA", "S":"XMAS"}
    if letter in expected_words and word != expected_words[letter]:
        return 0

    xmas_count = 1 if word == "XMAS" else 0
    return xmas_count + sum(dfs(chars, m, n, i + dx, j + dy, word, i, j, dirct if direction == "" else direction)
                            for dx, dy, dirct in dist)


letters = []
with open("input.txt", "r") as file:
    for line in file:
        letters.append(list(line.replace("\n", "")))

    row = len(letters)
    col = len(letters[0])
    dist = {(-1, -1, "UP_LEFT"), (-1, 0, "UP"), (-1, 1, "UP_RIGHT"), (0, -1, "LEFT"), (0, 1, "RIGHT"),
            (1, -1, "BOTTOM_LEFT"), (1, 0, "BOTTOM"), (1, 1, "BOTTOM_RIGHT")}

    xmas = sum(
        dfs(letters, row, col, x + dx, y + dy, "X", x, y, direction)
        for x in range(row)
        for y in range(col) if letters[x][y] == "X"
        for dx, dy, direction in dist)

    print(xmas)
