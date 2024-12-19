from nis import match

with open("input/advent17.txt", "r") as file:
    for line in file:
        if "Register A:" in line:
            A = int(line.strip().replace("Register A:", ""))
        elif "Register B:" in line:
            B = int(line.strip().replace("Register B:", ""))
        elif "Register C:" in line:
            C = int(line.strip().replace("Register C:", ""))
        elif "Program:" in line:
            program = list(map(int, line.strip().replace("Program:", "").split(",")))


def get_combo(operand, op_A, op_B, op_C):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return op_A
    if operand == 5:
        return op_B
    if operand == 6:
        return op_C


def calc(new_A, new_B, new_C):
    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        pointer += 1
        operand = program[pointer]
        pointer += 1

        combo = get_combo(operand, new_A, new_B, new_C)

        if opcode == 0:  # adv, combo
            new_A = new_A // (2 ** combo)
        elif opcode == 1:  # bxl, literal
            new_B = new_B ^ operand
        elif opcode == 2:  # bst, combo
            new_B = combo % 8
        elif opcode == 3:  # jump, literal
            if new_A != 0:
                pointer = operand
        elif opcode == 4:  # bxc, ignore operand
            new_B = new_B ^ new_C
        elif opcode == 5:  # out, combo
            res = combo % 8
            output.append(str(res))
        elif opcode == 6:  # bdv, combo
            new_B = new_A // (2 ** combo)
        elif opcode == 7:  # cdv, combo
            new_C = new_A // (2 ** combo)
    return output


print(calc(A, 0, 0))

for i in range(0, 1000000):
    values = calc(A + i, 0, 0)
    if ",".join(values) == "2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0":
        print("Found", A + i)
    # print("For", i, ",".join(values))
