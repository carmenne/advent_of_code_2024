order = set()
pages = []

with open("input.txt", "r") as file:
    for line in file:
        if "|" in line:
            order.add(line.strip())
        elif line.strip() != "":
            pages.append(line.strip().split(","))

result = 0
for page in pages:
    N = len(page)
    mid = N // 2
    print(N)
    ordered = True
    for i in range(N):
        for j in range(i, N):
            if page[j] + "|" + page[i] in order:
                # reversed
                ordered = False
    result += int(page[mid]) if ordered else 0

print(result)
