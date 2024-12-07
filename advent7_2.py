operations = []
import time


def calculate(numbers, count, op, total, target, result):
    if count == len(numbers):
        if total == target:
            print("Add result", op, total)
            result.append(target)
        return

    calculate(numbers, count + 1, op + "+", total + numbers[count], target, result)
    calculate(numbers, count + 1, op + "||", int("0" if total == 0 else str(total) + str(numbers[count])), target, result)
    calculate(numbers, count + 1, op + "*", (1 if total == 0 else total) * numbers[count], target, result)


with (open("input.txt", "r") as file):
    for line in file:
        target, operators = line.strip().split(":")
        op = []
        op.append(int(target))
        op += list(map(int, operators.strip().split(" ")))
        operations.append(op)

    results = []
    print(len(operations))
    start_time = time.time()

    for operators in operations:
        target = operators[0]
        numbers = operators[1:]
        N = len(numbers)

        result = []
        calculate(numbers, 0, "", 0, target, result)
        print("result", result)

        if result and target == result[0]:
            results.append(target)

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime:.6f} seconds")
    print(results)
    print("sum", sum(results))

