dist1 = []
dist2 = []

input_file="input.txt"
with open(input_file, "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        dist1.append(num1)
        dist2.append(num2)

dist1.sort()
dist2.sort()

dist = 0
for i in range(0, len(dist1)):
    if dist1[i] > dist2[i]:
        dist += dist1[i] - dist2[i]
    else:
        dist += dist2[i] - dist1[i]

print(dist)
