
winning_numbers = []
my_numbers = []
with open("input.txt", "r") as file:
    for line in file:
        line_strip = line.strip()
        idx = line_strip.find(":")
        just_numbers = line_strip[idx + 1:]
        numbers = line.split(":")[1].strip().split("|")
        winning_numbers.append(list(map(int, numbers[0].replace("  ", " ").strip().split(" "))))
        split = numbers[1].replace("  ", " ").strip().split(" ")
        my_numbers.append(list(map(int, split)))

total = 0
for i in range(len(winning_numbers)):
    winning = set(winning_numbers[i])
    mine = set(my_numbers[i])

    common = winning.intersection(mine)
    if len(common) > 0:
        common_ = 2 ** (len(common) - 1)
        total += common_

print(int(total)) # 15205

