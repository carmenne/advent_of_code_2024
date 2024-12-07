operations = []
import time

with (open("input.txt", "r") as file):
    for line in file:
        target, operators = line.strip().split(":")
        op = [int(target)]
        op += list(map(int, operators.strip().split(" ")))
        operations.append(op)

    results = []
    start_time = time.time()

    targets = []
    for operators in operations:
        target = operators[0]
        numbers = operators[1:]
        N = len(numbers)

        results = set()
        results.add(numbers[0])
        print(numbers[0])

        for number in numbers[1:]:
            new_results = set()
            for result in results:
                new_result = result + number
                if new_result <= target:
                    new_results.add(new_result)
                new_result = result * number
                if new_result <= target:
                    new_results.add(new_result)
                new_result = int(str(result) + str(number))
                if new_result <= target:
                    new_results.add(new_result)

            results = new_results

        for result in results:
            if result == target:
                targets.append(target)

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime:.6f} seconds")
    print("sum", sum(targets))
