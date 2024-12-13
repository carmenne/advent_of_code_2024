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
            prizes.append((int( xy[0].replace("X=", "")), int(xy[1].replace("Y=", ""))))

def calc_tokens(prize, push):

    if prize in memo:
        return memo[prize]

    if push > 200:
        return float("inf"), float("inf")
    x_p, y_p = prize

    if x_p == 0 and y_p == 0:
        return 0, 0
    if x_p < 0 or y_p < 0:
        return float("inf"), float("inf")

    x_a, y_a = button_a
    x_b, y_b = button_b

    a1, b1 = calc_tokens((x_p - x_a, y_p - y_a), push + 1)
    a2, b2 = calc_tokens((x_p - x_b, y_p - y_b), push + 1)

    if (a1 + 1) + b1 < a2 + b2 + 1:
        result = (a1 + 1, b1)
    else:
        result = (a2, b2 + 1)
    memo[prize] = result
    print("Push", push, memo[prize] if prize in memo else None, "for", x_p, y_p)
    return result


total = 0
for button_a, button_b, p in zip(buttons_a, buttons_b, prizes):
    memo = {}
    a,b = calc_tokens(p, 0)
    if a != float("inf"):
        total += a * 3 + b

print("Total", total)
