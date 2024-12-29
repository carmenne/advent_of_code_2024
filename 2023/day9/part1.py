def forecast(history):
    k, last = 1, 0
    history_it = history
    while set(history_it) != {0}:
        history_it = [history_it[i] - history_it[i - 1] for i in range(1, len(history) - k + 1)]
        last += history_it[-1]
        k += 1

    return history[-1] + last


with open("input_long.txt", "r") as file:
    print(sum(forecast([int(number) for number in line.strip().split(" ")]) for line in file))
    # 1993300041
