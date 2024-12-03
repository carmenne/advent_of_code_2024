import re

with open("input.txt", "r") as file:
    file_content = file.read().replace("\n", "")
    final_content = re.sub("don't\(\).+?do\(\)", "", file_content).split("don't")[0]
    mulls = re.findall("mul\([0-9]+,[0-9]+\)", final_content)

result = 0
for mul in mulls:
    numbers = mul.replace("mul(", "").replace(")", "")
    num1, num2 = numbers.split(",")
    result += int(num1) * int(num2)
print(len(mulls), result)
