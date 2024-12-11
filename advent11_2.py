def split_stone(stone, blink, blinks):
    if blink == 0:
        return 1

    if (stone, blink) in blinks:
        return blinks[(stone, blink)]

    if stone == 0:
         result = split_stone(1, blink - 1, blinks)
    elif (st_len:= len(str(stone))) % 2 == 0:
        mid = st_len // 2
        stone1 = str(stone)[:mid]
        stone2 = str(stone)[mid:]
        result = split_stone(int(stone1), blink - 1, blinks) + split_stone(int(stone2), blink - 1, blinks)

    else:
        result = split_stone(stone * 2024, blink - 1, blinks)

    blinks[(stone, blink)] = result
    return result


stones = []
with open("input.txt", "r") as file:
    stones += map(int, file.read().strip().split())

total = 0

blinks = {}
for gem in stones:
    total += split_stone(gem, 75, blinks)

print(total)
