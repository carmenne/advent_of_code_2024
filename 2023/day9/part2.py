histories = []
with open("input_long.txt", "r") as file:
    for line in file:
        histories.append([int(number) for number in line.strip().split(" ")])

def not_zero(difference):
    return difference and difference != {0}

def get_prev_element(forecast_data):
    prev = forecast_data[-1]
    for i in range(len(forecast_data) - 2, -1, -1):
        prev = forecast_data[i] - prev
    return prev

prev_elements = []
for history in histories:

    k = 1
    not_all_zeroes = True
    history_it = history
    first = []
    length = len(history)
    while not_all_zeroes:
        difference = []
        for i in range(1, length - k + 1):
            dif = history_it[i] - history_it[i-1]
            difference.append(dif)
        history_it = difference

        if not_zero(set(difference)):
            first.append(difference[0])

        k += 1
        not_all_zeroes = not_zero(set(difference))

    forecast_data = [history[0]]
    forecast_data.extend(first)
    prev_elements.append(get_prev_element(forecast_data))

print(sum(prev_elements)) # 1038