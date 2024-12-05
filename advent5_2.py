from advent5_1 import result

order = set()
pages = []

with open("input.txt", "r") as file:
    for line in file:
        if "|" in line:
            order.add(line.strip())
        elif line.strip() != "":
            pages.append(line.strip().split(","))

unordered_pages = []
for page in pages:
    N = len(page)
    ordered = True
    for i in range(N):
        for j in range(i, N):
            if page[j] + "|" + page[i] in order:
                # reversed
                ordered = False
    if not ordered:
        unordered_pages.append(page)


def swap(a, k, l):
    tmp = a[k]
    a[k] = a[l]
    a[l] = tmp

result = 0

for page in unordered_pages:
    N = len(page)
    ordered = True
    for i in range(N):
        for j in range(i, N):
            if page[j] + "|" + page[i] in order:
                # reversed
                swap(page, i, j)
    result += int(page[N // 2]) if ordered else 0
print(result)
