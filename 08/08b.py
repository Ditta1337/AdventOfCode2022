with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/08/input.txt') as f:
    data = f.readlines()

# uses much space, but I dont give a fuck
# O(n^3) im disgusted

dataTab = [[0 for _ in range(len(data[0]) - 1)] for _ in range(len(data))]
tab = [[[] for _ in range(len(data[0]) - 1)] for _ in range(len(data))]


def fillTab(data):
    for index_y, line in enumerate(data):
        for index_x, height in enumerate(line):
            if height != '\n':
                dataTab[index_y][index_x] = int(height)


def fromLeft(dataTab, index_x, index_y):
    counter = 0
    if index_x == 0:
        tab[index_y][index_x].append(0)
        return
    for i in range(index_x - 1, -1, -1):
        if dataTab[index_y][i] < dataTab[index_y][index_x]:
            counter += 1
        else:
            counter += 1
            break
    tab[index_y][index_x].append(counter)


def fromRight(dataTab, index_x, index_y):
    counter = 0
    if index_x == len(dataTab[0]) - 1:
        tab[index_y][index_x].append(0)
        return
    for i in range(index_x + 1, len(dataTab[0])):
        if dataTab[index_y][i] < dataTab[index_y][index_x]:
            counter += 1
        else:
            counter += 1
            break
    tab[index_y][index_x].append(counter)


def fromTop(dataTab, index_x, index_y):
    counter = 0
    if index_y == 0:
        tab[index_y][index_x].append(0)
        return
    for i in range(index_y - 1, -1, -1):
        if dataTab[i][index_x] < dataTab[index_y][index_x]:
            counter += 1
        else:
            counter += 1
            break
    tab[index_y][index_x].append(counter)


def fromBottom(dataTab, index_x, index_y):
    counter = 0
    if index_y == len(dataTab) - 1:
        tab[index_y][index_x].append(0)
        return
    for i in range(index_y + 1, len(dataTab)):
        if dataTab[i][index_x] < dataTab[index_y][index_x]:
            counter += 1
        else:
            counter += 1
            break
    tab[index_y][index_x].append(counter)


def applyAll(dataTab):
    for index_y, line in enumerate(dataTab):
        for index_x, _ in enumerate(line):
            fromLeft(dataTab, index_x, index_y)
            fromRight(dataTab, index_x, index_y)
            fromTop(dataTab, index_x, index_y)
            fromBottom(dataTab, index_x, index_y)


def returnRet(tab):
    max = 0
    for rows in tab:
        for cols in rows:
            tmp = 1
            for distance in cols:
                tmp *= distance
            if tmp > max:
                max = tmp
    return max


fillTab(data)
applyAll(dataTab)
print(returnRet(tab))

f.close()
