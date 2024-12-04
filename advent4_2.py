def xmas_shape(letters, i, j):

    if letters[i + 1][j + 1] != "A":
        return 0

    if letters[i][j] == "M" and letters[i + 2][j + 2] == "S" and letters[i + 2][j] == "M" and letters[i][j+2] == "S":
       return 1

    if letters[i][j] == "S" and letters[i + 2][j + 2] == "M" and letters[i + 2][j] == "S" and letters[i][j+2] == "M":
        return 1

    if letters[i][j] == "M" and letters[i + 2][j + 2] == "S" and letters[i + 2][j] == "S" and letters[i][j+2] == "M":
            return 1

    if letters[i][j] == "S" and letters[i + 2][j + 2] == "M" and letters[i + 2][j] == "M" and letters[i][j+2] == "S":
        return 1

    return 0

letters = []
with open("input.txt", "r") as file:
    for line in file:
        letters.append(list(line.replace("\n", "")))

    X_MASes = 0
    row = len(letters)
    column = len(letters[0])
    for x in range(row - 2):
        for y in range(column - 2):
                X_MASes += xmas_shape(letters, x, y)
    print(X_MASes)
