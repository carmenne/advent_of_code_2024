safe = 0

input_file="input.txt"


def test_safe_increasing(numbers):
    is_safe = True
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] < 1 or numbers[i] - numbers[i-1] > 3:
            is_safe = is_safe and False

    return is_safe


def test_safe_decreasing(numbers):
    is_safe = True
    for i in range(1, len(numbers)):
        if numbers[i-1] - numbers[i] < 1 or numbers[i-1] - numbers[i] > 3:
            is_safe = is_safe and False;

    return is_safe


def count_safe(numbers):
    count = 0
    if numbers[1] > numbers[0]: #increasing
        if test_safe_increasing(numbers):
            count += 1
    else: #decreasing
        if test_safe_decreasing(numbers):
            count += 1

    return count


with open(input_file, "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if count_safe(numbers) == 1:
            safe += 1
        else:
            for i in range(0, len(numbers)):
                # remove element at i
                new_numbers = numbers[:i] + numbers[i+1:]
                print(new_numbers)
                if count_safe(new_numbers) == 1:
                    safe += 1
                    break

    print(safe)
