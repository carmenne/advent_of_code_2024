input = []
with open("input/advent22.txt", "r") as file:
    for line in file:
        input.append(line.strip())

print(len(input))

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

total = 0

def generate_secrets(number):
    num = int(number)
    for i in range(2000):
        res = secret(num)
        num = res
    return res

for number in input:
    total += generate_secrets(number)

print(total) # 14273043166

