sequences = ""
with open("input_long.txt", "r") as file:
    for line in file:
        sequences = line.strip().split(",")

def ascii_code(seq):
    code = 0
    for s in list(seq):
        code = ((code + ord(s)) * 17) % 256
    return code

result = 0
for seq in sequences:
    result += ascii_code(seq)
print(result) # 507666