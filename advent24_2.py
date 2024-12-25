variables = {}
instructions = {}
with open("input/advent24.txt") as file:
    for line in file:
        if ":" in line:
            name, val = line.strip().split(":")
            variables[name.strip()] = name.strip()
        elif line != "\n":
            inst, res = line.strip().split("->")
            op1, op, op2 = inst.strip().split(" ")
            if op1[:1] == "x":
                op1, op2 = op2, op1
            instructions[res.strip()] = (op1 + " " + op + " " + op2)


def calc(op1, op, op2):
    if len(variables[op1]) < len(variables[op2]):
        return "(" + variables[op1] + " " + op + " " + variables[op2] + ")"
    else:
        return "(" + variables[op2] + " " + op + " " + variables[op1] + ")"


def execute_instructions(instructions_set):
    for i in range(0, 46):
        for result, instruction in instructions_set.copy().items():
            op1, op, op2 = instruction.strip().split(" ")
            if op1 in variables and op2 in variables:
                result_value = calc(op1, op, op2)
                variables[result.strip()] = result_value


zs = {}
first_swap = instructions.copy()
tmp = first_swap["z08"]
first_swap["z08"] = first_swap["mvb"]
first_swap["mvb"] = tmp
tmp = first_swap["jss"]
first_swap["jss"] = first_swap["rds"]
first_swap["rds"] = tmp
tmp = first_swap["z18"]
first_swap["z18"] = first_swap["wss"]
first_swap["wss"] = tmp
tmp = first_swap["z23"]
first_swap["z23"] = first_swap["bmn"]
first_swap["bmn"] = tmp
instructions = first_swap.copy()


execute_instructions(instructions.copy())
for v in variables:
    if v[:1] == "z":
        zs[v] = variables[v]



r = ["z08", "z18", "z23", "jss", "rds", "mvb", "bmn", "wss"]
print(",".join(sorted(r)))

m = 0
for item in sorted(zs.items()):
    if m < 18:
        print(item)
    m += 1

z00 = "(x00 XOR y00)"
z01 = "((x00 AND y00) XOR (x01 XOR y01)))"


def find_other(variables, zk):
    for k, v in variables.items():
        if v == zk: return k

    return "Not found"


for k in range(2, 45):
    prev_k = "0" + str(k - 1) if k - 1 < 10 else str(k - 1)
    curr_k = "0" + str(k) if k < 10 else str(k)
    z_ = variables["z" + prev_k]
    const_z = "((" + variables["x" + curr_k] + " XOR " + variables["y" + curr_k] + ")"
    zk = (const_z +
          " XOR " +
          "((" + variables["x" + prev_k] + " AND " + variables["y" + prev_k] + ")" +
          " OR " + z_[:14] + " AND " + z_[19:]) + "))"

    already_zk = variables["z" + curr_k]
    if zk != already_zk:
        print("difference found", "z" + curr_k)
        print(already_zk)
        print(zk)
        print("Candidate for", const_z)
        print(find_other(variables, zk))
        print(find_other(variables, const_z))
