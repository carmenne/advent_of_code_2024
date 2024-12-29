steps = {}
with open("input_long.txt", "r") as file:
    for line in file:
        if "=" in line:
            a, b = line.strip().split("=")
            l, r = b.replace("(", "").replace(")", "").strip().split(", ")
            steps[a.strip()] = (l, r)
        elif line != "\n":
            sequence = list(line.strip())

print(sequence)
print(steps)

step = "AAA"
taken_steps = 0
while step != "ZZZ":
    for seq in sequence:
        if seq == "L":
            step = steps[step][0]
        else:
            step = steps[step][1]
        taken_steps += 1
        if step == "ZZZ":
            break

print(taken_steps) # 20513