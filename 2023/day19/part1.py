workflows = {}
ratings = []
with open("input_long.txt", "r") as file:
    for line in file:

        if not line.startswith("{") and "{" in line:
            wk_name, wk_rule = line.strip().split("{")
            workflows[wk_name] = wk_rule.replace("}", "").split(',')
        elif line.startswith("{"):
            rating = line.strip().replace("}", "").replace("{", "").split(",")
            ratings.append([tuple(r.split("=")) for r in rating])

print(workflows)
print(ratings)

print("Start with 'in'")
print(workflows.get("in"))


def apply(left, op, right):
    if op == "<":
        return int(left) < int(right)
    elif op == ">":
        return int(left) > int(right)


def match_if(rule, rating):
    left, op, right, wf = parse_wf(rule)

    for r in rating:
        variable, value = r
        if variable == left:
            matches = apply(value, op, right)
            if matches:
                return match_final(wf)

    return "N", ""


def parse_wf(rule):
    left = rule[:1]
    op = rule[1:2]
    idx = rule.find(":")
    right = rule[2:idx]
    wf = rule[idx + 1:]
    return left, op, right, wf


def match_final(rule):
    if rule == "A":
        return "A", ""
    elif rule == "R":
        return "R", ""
    return "M", rule


accepted = []
for rating in ratings:

    workflow = workflows["in"]
    while workflow:
        for rule in workflow:
            if ":" in rule:
                status, wf = match_if(rule, rating)
            else:
                status, wf = match_final(rule)

            if status == "M":
                workflow = workflows[wf]
                break
            elif status == "N":
                continue
            elif status == "A":
                accepted.append(rating)
                workflow = False
                break
            else:  # REJECTED
                workflow = False
                break

    print(accepted)

print(accepted)

total = 0
for rating in accepted:
    total_per_rating = 0
    for r in rating:
        variable, value = r
        total_per_rating += int(value)
    print("Rating", total_per_rating)
    total += total_per_rating

print(total) # 342650
