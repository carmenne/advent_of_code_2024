buttons_a = []
buttons_b = []
prizes = []
with open("input.txt", "r") as file:
    for line in file:
        if "Button A" in line:
            nl = line.replace("Button A:", "")
            xy = nl.split(",")

            buttons_a.append((int(xy[0].replace("X+", "")), int(xy[1].replace("Y+", ""))))

        if "Button B" in line:
            nl = line.replace("Button B:", "")
            xy = nl.split(",")
            buttons_b.append((int(xy[0].replace("X+", "")), int(xy[1].replace("Y+", ""))))

        if "Prize:" in line:
            nl = line.replace("Prize:", "")
            xy = nl.split(",")
            prizes.append((10000000000000 + float(xy[0].replace("X=", "")), 10000000000000 + float(xy[1].replace("Y=", ""))))

print(prizes)
def calc_tokens(prize):

    p1, p2 = prize
    x1, x2 = button_a
    y1, y2 = button_b

    if (b:= (p2 * x1 - p1 * x2) // (y2 * x1 - x2 * y1)) == (p2 * x1 - p1 * x2) / (y2 * x1 - x2 * y1):
        print("b", b, p1, p2, x1, y1, x2, y2, p2 * x1, p1 * x2)
        if (a:= (p1 - b * y1) // x1) == (p1 - b * y1) / x1:
            return a, b

    return 0, 0


total = 0
for button_a, button_b, p in zip(buttons_a, buttons_b, prizes):
    memo = {}
    a,b = calc_tokens(p)
    if a != float("inf"):
        total += a * 3 + b

print("Total", total)
