disk_map = ""

expanded = []

with open("input.txt") as file:
    disk_map = file.read().replace("\n", "")

    # determine expanded view of the disks
    i = 0
    file_id = 0
    disks = list(disk_map)
    occ = {}
    sort_by_id = {}
    for point in disks:
        if i % 2 == 0:
            file_i = len(expanded)
            expanded += [file_id] * int(disks[i])
            occ[file_id] = (int(disks[i]), file_i + 1) # length, start position
            file_id += 1
        else:
            expanded += ["."] * int(disks[i])
        i += 1

    # compact it
    # Start from end, and when finding a position, put it there
    m = len(occ) - 1
    while m > 0:
        file_len, file_idx = occ[m]
        to_fill = m
        # fill it

        # find a fitting position
        dot_start = -1
        dot_end = -1
        fitting = False
        i = 0
        while i < len(expanded):
            if expanded[i] == ".":
                if dot_start == -1:
                    dot_start = i
                if dot_end == -1:
                    dot_end = i
                else:
                    dot_end += 1

            if dot_end != -1 and (dot_end - dot_start + 1) >= file_len:
                fitting = True

            if fitting:
                if file_idx >= dot_start:
                    for k in range(dot_start, dot_start + file_len):
                        expanded[k] = to_fill
                        expanded[file_idx + (k - dot_start) - 1] = "F"
                break

            if expanded[i] != ".":
                dot_start = -1
                dot_end = -1
            i += 1

        m -= 1

    # calculate checksum
    checksum = 0
    j = 0
    while j < len(expanded):
        if expanded[j] != "." and expanded[j] != "F":
            checksum += j * int(expanded[j])
        j += 1

    print(checksum)
