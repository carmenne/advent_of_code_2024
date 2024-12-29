import math

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


def go_to_end(start):
    taken_steps = 0
    step = start
    while step[-1] != "Z":
        for seq in sequence:
            if seq == "L":
                step = steps[step][0]
            else:
                step = steps[step][1]
            taken_steps += 1
            if step[-1] == "Z":
                break

    return taken_steps


numbers = []
for step in steps:
    if step[-1] == "A":
        numbers.append(go_to_end(step))

print(numbers)
print(math.lcm(*numbers))  # 15995167053923
print(math.prod(numbers))


def my_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def my_lcm(numbers):
    prev = numbers[0]
    for i in range(1, len(numbers)):
        min_num = min(prev, numbers[i])
        max_num = max(prev, numbers[i])
        gcd_num = my_gcd(prev, numbers[i])
        prev = min_num * (max_num // gcd_num)
    return prev

print(my_lcm([4, 6, 8]))
print(my_lcm(numbers))
