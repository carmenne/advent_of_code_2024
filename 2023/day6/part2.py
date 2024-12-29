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