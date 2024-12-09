disk_map = ""

expanded = []
with open("input.txt") as file:
    disk_map = file.read().replace("\n", "")

    i = 0
    file = 0
    disks = list(disk_map)
    ex_sum = 0
    for point in disks:
        if i % 2 == 0:
            expanded += [file] * int(disks[i])
            ex_sum += file * int(disks[i])
            file += 1
        else:
            expanded += ["."] * int(disks[i])
        i += 1

    map_len = len(expanded)
    start = 0
    end = map_len - 1

    while start < end:
        while expanded[start] != ".":
            start += 1
        while expanded[end] == ".":
            end -= 1
        expanded[start] = int(expanded[end])
        expanded[end] = "."
        start += 1
        end -= 1

    checksum = 0
    j = 0
    pos = 0
    while j < len(expanded):
        if expanded[j] != ".":
            checksum += j * int(expanded[j])
            pos += 1
        j += 1

    print(checksum)

