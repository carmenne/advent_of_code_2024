sequences = ""
with open("input_long.txt", "r") as file:
    for line in file:
        sequences = line.strip().split(",")


def ascii_code(seq):
    code = 0
    for s in list(seq):
        code = ((code + ord(s)) * 17) % 256
    return code


HASHMAP = [{} for i in range(256)]
for seq in sequences:
    if "=" in seq:
        l, r = seq.split("=")
        box = ascii_code(l)
        HASHMAP[box][l] = r
    elif "-" in seq:
        l = seq.replace("-", "")
        box = ascii_code(l)
        box_ = HASHMAP[box]
        if l in box_:
            del box_[l]

total = 0
for box_idx in range(1, 257):
    box = HASHMAP[box_idx - 1]
    i = 1
    for k, v in box.items():
        total += box_idx * i * int(v)
        i += 1

print(total)
