with open('./01/input.txt') as f:
    data = f.readlines()

tab = []
counter = 0
ret = 0
tmp = 0

for line in data:
    if line != '\n':
        tmp += int(line)
    else:
        if counter != 3:
            tab.append([tmp, counter])
            counter += 1
            print(tab)
        else:
            if min(tab)[0] < tmp:
                tab[min(tab)[1]][0] = tmp
        tmp = 0

for elem in tab:
    ret += elem[0]

print(ret)
f.close()
