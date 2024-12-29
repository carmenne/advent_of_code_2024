histories = []
with open("input_long.txt", "r") as file:
    for line in file:
        histories.append([int(number) for number in line.strip().split(" ")])

def not_zero(difference):
    return difference and difference != {0}

next_elements = []
for history in histories:

    k = 1
    not_all_zeroes = True
    history_it = history
    last = []
    length = len(history)
    while not_all_zeroes:

        difference = []
        for i in range(1, length - k + 1):
            dif = history_it[i] - history_it[i-1]
            difference.append(dif)
        history_it = difference
        last.append(difference[-1])

        k += 1
        not_all_zeroes = not_zero(set(difference))

    next_elements.append(history[-1] + sum(last))

print(sum(next_elements)) # 1993300041