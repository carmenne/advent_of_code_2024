safe = 0

input_file="input.txt"
with open(input_file, "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if numbers[1] > numbers[0]: #increasing
            is_safe = True
            for i in range(1, len(numbers)):
                if numbers[i] - numbers[i-1] < 1 or numbers[i] - numbers[i-1] > 3:
                    is_safe = is_safe and False
            if is_safe:
                safe += 1

        else: #decreasing
            is_safe = True
            for i in range(1, len(numbers)):
                if numbers[i-1] - numbers[i] < 1 or numbers[i-1] - numbers[i] > 3:
                    is_safe = is_safe and False;
            if is_safe:
                safe += 1

    print(safe)
