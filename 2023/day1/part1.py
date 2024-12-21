inputs = []
with open("input.txt", "r") as file:
    for line in file:
        inputs.append(line.strip())

total = 0
for line in inputs:
    start = 0
    while start < len(line):
        if line[start] in "123456789":
            break
        start += 1

    end = len(line) - 1
    while end >= 0:
        if line[end] in "123456789":
            break
        end -= 1
    total += int(line[start] + line[end])

print(total)