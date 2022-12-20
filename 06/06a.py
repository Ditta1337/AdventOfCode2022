with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/06/input.txt') as f:
    data = f.readlines()[0]

ret = 0
tab = []

for ind, letter in enumerate(data):
    if len(tab) == 4:
        if len(tab) == len(set(tab)):
            ret = ind
            break
        tab.pop(0)
    tab.append(letter)

print(ret)

f.close()