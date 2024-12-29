from collections import defaultdict

camel_cards = []
with open("input_long.txt", "r") as file:
    for line in file:
        card, bid = line.strip().split(" ")
        camel_cards.append((card, int(bid)))


def put_J_end(cards):
    new_cards = ""
    js = ""
    for card in cards:
        if card == "J":
            js += "J"
        else:
            new_cards += card

    return new_cards + js


def get_hand_type(cards):
    distinct = defaultdict(int)
    cards = put_J_end(cards)
    for card in cards:
        if card == "J" and distinct:
            print(cards)
            max_freq = max(distinct, key=distinct.get)
            distinct[max_freq] += 1
        else:
            distinct[card] += 1

    ranks = {"11111" : "1", "1112" : "2", "122": "3", "113": "4", "23": "5", "14": "6", "5": "7"}
    freq = "".join([str(value) for value in sorted(distinct.values())])
    return ranks[freq]



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
