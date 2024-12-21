VALID_WORDS = {"one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
VALID_LEN_3 = {"one", "two", "six"}
VALID_LEN_4 = {"four", "five", "nine"}
VALID_LEN_5 = {"three", "seven", "eight"}

inputs = []
with open("input.txt", "r") as file:
    for line in file:
        inputs.append(line.strip())

def extract_first(line):
    for start in range(0, len(line)):
        if line[start] in "123456789":
            return line[start]
        if start >= 2:
            if line[start - 2:start + 1] in VALID_LEN_3:
                return VALID_WORDS[line[start - 2:start + 1]]
        if start >= 3:
            if line[start - 3:start + 1] in VALID_LEN_4:
                return VALID_WORDS[line[start - 3:start + 1]]
        if start >= 4:
            if line[start - 4:start + 1] in VALID_LEN_5:
                return VALID_WORDS[line[start - 4:start + 1]]


def extract_last(line):
    n = len(line)
    for end in range(n - 1, -1, -1):
        if line[end] in "123456789":
            return line[end]
        if end <= n - 3:
            if line[end:end + 3] in VALID_LEN_3:
                return VALID_WORDS[line[end:end + 3]]
        if end <= n - 4:
            if line[end:end + 4] in VALID_LEN_4:
                return VALID_WORDS[line[end:end + 4]]
        if end <= n - 5:
            if line[end:end + 5] in VALID_LEN_5:
                return VALID_WORDS[line[end:end + 5]]


total = sum(int(extract_first(inpt) + extract_last(inpt)) for inpt in inputs)
print(total)  # 54980
