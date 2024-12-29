with open("input_long.txt", "r") as file:
    for line in file:
        if "Time:" in line:
            times = [int(time) for time in line.strip().split(":")[1].strip().split("     ")]
        elif "Distance:" in line:
            distances = [int(distance) for distance in line.strip().split(":")[1].strip().split("   ")]

print(times, distances)

products = 1
for time, distance in zip(times, distances):
    product = 0
    for i in range(time + 1):

        speed = i
        if speed * (time - i) > distance:
            product += 1

    if product:
        products *= product

print(products) # 4811940