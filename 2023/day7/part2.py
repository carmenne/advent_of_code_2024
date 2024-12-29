from collections import defaultdict

camel_cards = []
with open("input_long.txt", "r") as file:
    for line in file:
        card, bid = line.strip().split(" ")
        camel_cards.append((card, int(bid)))


def get_hand_type(cards):
    distinct = defaultdict(int)
    for card in cards:
        distinct[card] += 1


    freq = sorted(distinct.values())
    if len(distinct) == 1 or (len(distinct) == 2 and "J" in cards):
        return 7
    elif len(distinct) == 2:
        if freq == [1, 4]:
            return 6
        else:
            return 5
    elif len(distinct) == 3:
        if freq == [1, 1, 3]:
            return 6 if "J" in cards else 4
        else:
            if distinct["J"] == 1:
                return 5
            elif distinct["J"] == 2:
                return 6
            return 3
    elif len(distinct) == 4:
        return 4 if "J" in cards else 2
    else:
        return 2 if "J" in cards else 1


score = {"A": "m", "K": "l", "Q": "k", "T": "i", "9": "h", "8": "g", "7": "f", "6": "e", "5": "d"
    , "4": "c", "3": "b", "2": "a", "J": "0"}


def get_card_score(cards):
    score_card = ""
    for card in cards:
        score_card += score[card]
    return score_card


def compare_types(cards):
    type = get_hand_type(cards[0])
    card_score = get_card_score(cards[0])

    return str(type) + card_score


print("Before sorting", camel_cards)
camel_cards.sort(key=compare_types)
print("After sorting", camel_cards)

total = 0
for i in range(1, len(camel_cards) + 1):
    total += i * camel_cards[i - 1][1]

print(total)  # 253907829
