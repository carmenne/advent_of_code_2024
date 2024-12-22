import heapq

input = []
with open("input/advent22_3.txt", "r") as file:
    for line in file:
        input.append(line.strip())

def mix(num, secret_num):
    return num ^ secret_num

def prune(secret_num):
    return secret_num % 16777216

def secret(secret_num):
    S2 = secret_num * 64
    secret_num = mix(secret_num, S2)
    secret_num = prune(secret_num)

    S3 = secret_num // 32
    secret_num = mix(secret_num, S3)
    secret_num = prune(secret_num)

    S4 = secret_num * 2048
    secret_num = mix(secret_num, S4)
    secret_num = prune(secret_num)

    return secret_num


def generate_secrets(number, limit):
    num = int(number)
    for i in range(limit):
        res = secret(num)
        num = res
    return res


def generate_ones(number, limit):
    num = int(number)
    ones = []
    for i in range(limit):
        res = secret(num)
        ones.append(res % 10)
        num = res
    return ones

difs = {-9: "a", -8: "b", -7: "c", -6: "d", -5: "e", -4: "f", -3: "g", -2: "h", -1: "i", 0: "j", 1: "k", 2: "l", 3: "m", 4: "n", 5: "o", 6: "p", 7: "q", 8: "r", 9: "s"}
difs_reversed = {"a": -9, "b": -8, "c": -7, "d": -6, "e": -5, "f": -4, "g": -3, "h": -2, "i": -1, "j": 0, "k": 1, "l": 2, "m": 3, "n": 4, "o": 5, "p": 6, "q": 7, "r": 8, "s": 9}

def map_letters_to_numbers(change_string):
    return [difs_reversed[char] for char in change_string]
def map_numbers_to_letter(change):
    return "".join([difs[char] for char in change])

def get_ones_changes(ones):
    ones_changes = ""
    for i in range(1, len(ones)):
        ones_changes += difs[ones[i] - ones[i - 1]]
    return ones_changes

def sell(changes, ones_changes):
    find = ones_changes.find(changes)
    return find + 4 if find >= 3 else -1

LIMIT = 2000
precomputed_ones = [generate_ones(number, LIMIT) for number in input]
precomputed_ones_changes = ["".join(get_ones_changes(ones)) for ones in precomputed_ones]


def generate_sequence_all_possible():
    sequences = []
    for i1 in range(-9,10):
        for i2 in range(-9,10):
            for i3 in range(-9,10):
                for i4 in range(-9,10):
                    sequences.append(difs[i1] + difs[i2] + difs[i3] + difs[i4])
    return sequences


def generate_sequence_all():
    sequences = set()
    for precomputed_one in precomputed_ones:
        for k in range(4, LIMIT):
            one = get_ones_changes(precomputed_one[k-4:k+1])
            sequences.add(one)

    return sequences

def generate_freq():
    freq = {}
    for precomputed_one in precomputed_ones:
        for k in range(4, LIMIT):
            one = get_ones_changes(precomputed_one[k-4:k+1])
            if one in freq:
                freq[one] += 1
            else:
                freq[one] = 1

    return freq


def compute_bananas():
    freq = {}
    for precomputed_one in precomputed_ones:
        for k in range(4, LIMIT):
            one = get_ones_changes(precomputed_one[k-4:k+1])
            if one in freq:
                freq[one] += 1
            else:
                freq[one] = 1

    return freq

sequences = generate_freq()
max_bananas = 0
m = 0
cache = {}
for change, _ in sorted(sequences.items(), key=lambda kv: kv[1], reverse=True):
    bananas = 0
    for j in range(len(input)):
        sell_price_idx = sell(change, precomputed_ones_changes[j])
        if 0 <= sell_price_idx < 2000:
            sell_price = precomputed_ones[j][sell_price_idx]
            bananas += sell_price
    if bananas > max_bananas:
        max_bananas = bananas
    print("Progress", m, "out of", len(sequences))
    m += 1
    if m > 100:
        break

print(max_bananas) # 1667
