with open("input_long.txt", "r") as file:
    for line in file:
        if "Time:" in line:
            time = int(line.strip().split(":")[1].strip().replace(" ", ""))
        elif "Distance:" in line:
            distance = int(line.strip().split(":")[1].strip().replace(" ", ""))

print(time, distance)

product = 0
for i in range(time + 1):

    speed = i
    if speed * (time - i) > distance:
        product += 1

print(product)

# Quadratic equation
delta = math.sqrt(time ** 2 - 4 * distance)
d1 = (time - delta) // 2
d2 = (time + delta) // 2

print(d2 - d1) # 30077773
