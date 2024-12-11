stones = []
with open("input.txt", "r") as file:
    stones += map(int, file.read().strip().split())

total = 0
for blink in range(0, 25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        if stone == 0:
            stones[i] = 1
        elif (st_len:= len(str(stone))) % 2 == 0:
            mid = st_len // 2
            stone1 = str(stone)[:mid]
            stones[i] = int(stone1)
            stone2 = str(stone)[mid:]
            stones.insert(i + 1, int(stone2))
            i += 1
        else:
            stones[i] = stone * 2024
        i += 1
    # print(stones)

print(len(stones))
