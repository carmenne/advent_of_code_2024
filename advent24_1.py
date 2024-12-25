variables = {}
instructions = {}
with open("input/advent24.txt") as file:
    for line in file:
        if ":" in line:
            name, val = line.strip().split(":")
            variables[name.strip()] = int(val.strip())
        elif line != "\n":
            inst, res = line.strip().split("->")
            op1, op, op2 = inst.strip().split(" ")
            instructions[res.strip()] = (inst.strip())

def calc(op1, op, op2):
    if op == "AND":
        return op1 & op2
    elif op  == "XOR":
        return op1 ^ op2
    elif op == "OR":
        return op1 | op2


first_swap = instructions.copy()
print(first_swap)
res1 = "kfr"
res2 = "rwp"
tmp = first_swap[res1]
first_swap[res1] = first_swap[res2]
first_swap[res2] = tmp

instructions = first_swap.copy()
print(instructions)

while instructions:
    for result, instruction in instructions.copy().items():
        op1, op, op2 = instruction.strip().split(" ")
        if op1 in variables and op2 in variables:
            result_value = calc(variables[op1], op, variables[op2])
            variables[result.strip()] = result_value
            instructions.pop(result, None)

zs = {}
for k, v in variables.items():
    if "z" in k:
        zs[k] = v

all_z = zs.keys()
bits = ""
for z in sorted(all_z, reverse=True):
    bits += str(zs[z])
print(print(int(bits, 2))) # 41324968993486

print(41324968993486 - 41324960359118)
print('Dif {0:08b}'.format(41324968993486 - 41324960359118))
print(",".join(sorted(r)))
