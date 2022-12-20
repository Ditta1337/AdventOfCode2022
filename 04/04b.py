with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/04/input.txt') as f:
    data = f.readlines()

ret = 0

for line in data:
    symbols = ["" for _ in range(4)]
    index = 0
    for symbol in line:
        if symbol == "-" or symbol == "," or symbol == "\n":
            index += 1
        else:
            symbols[index] += symbol
    if int(symbols[0]) <= int(symbols[2]) and int(symbols[2]) <= int(symbols[1]) or int(symbols[0]) >= int(symbols[2]) and int(symbols[0]) <= int(symbols[3]):
        ret += 1

print(ret)
f.close()
