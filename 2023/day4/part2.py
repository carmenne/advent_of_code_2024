from collections import defaultdict

cards = defaultdict(int)
i = 1
with open("input.txt", "r") as file:
    for line in file:
        cards[i] += 1
        numbers = line.strip().split(":")[1].split("|")
        winning = set(numbers[0].split(" "))
        mine = set(numbers[1].split(" "))

        common = winning.intersection(mine)
        for j in range(1, len(common)):
            cards[i + j] += cards[i]

        i += 1

print("Total", sum(cards.values())) # 6189740
