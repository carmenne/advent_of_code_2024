dist1 = []
dist2 = []

input_file="input.txt"
with open(input_file, "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        dist1.append(num1)
        dist2.append(num2)

similarity = 0

# calculate freq
freq = {}
for dist in dist2:
    freq[dist] = freq.get(dist, 0) + 1

for dist in dist1:
    similarity += dist * freq.get(dist, 0)

print(similarity)
