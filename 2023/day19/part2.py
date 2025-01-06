workflows = {}
with open("input_long.txt", "r") as file:
    for line in file:

        if not line.startswith("{") and "{" in line:
            wk_name, wk_rule = line.strip().split("{")
            workflows[wk_name] = wk_rule.replace("}", "").split(',')

print(workflows)


def parse_wf(rule):
    left = rule[:1]
    op = rule[1:2]
    idx = rule.find(":")
    right = rule[2:idx]
    wf = rule[idx + 1:]
    return left, op, right, wf


xmas = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}


def accept(xmas):
    collect = 1
    for i1, i2 in xmas.values():
        collect *= abs(i2 - i1 + 1)
    return collect


def split_intv(interval, op, mid):
    i1, i2 = interval
    if op == "<":
        return (i1, int(mid) - 1), (int(mid), i2)
    else:
        return (int(mid) + 1, i2), (i1, int(mid))


def split(wf, xmas):
    if wf == "A":
        print("Accept", wf, xmas)
        return accept(xmas)
    if wf == "R":
        return 0

    result = 0
    for rule in workflows[wf]:
        if ":" in rule:
            rating, op, split_value, new_wf = parse_wf(rule)
            intv1, intv2 = split_intv(xmas[rating], op, split_value)

            xmas1 = xmas.copy()
            xmas1[rating] = intv1
            xmas[rating] = intv2
            result += split(new_wf, xmas1)
        else:
            result += split(rule, xmas)

    return result


print(split("in", xmas))
