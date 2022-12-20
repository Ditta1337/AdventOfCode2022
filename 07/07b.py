with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/07/input.txt') as f:
    data = f.readlines()

ind = [0]
tree = []
allSpace = 70000000
neededSpace = 30000000
freeSpace = 0
requiredSpace = 0
ret = [allSpace]


def rekFunc(data, ind, pos, length):
    while ind[0] < length:
        elems = data[ind[0]].split()
        ind[0] += 1
        if elems[0] == '$':
            if elems[1] == 'cd':
                if elems[2] == '..':
                    return
                else:
                    pos.insert(0, [])
                    rekFunc(data, ind, pos[0], length)
        elif elems[0] != 'dir':
            pos.append(int(elems[0]))


def rekFindUsed(tab):
    sum = 0
    for elem in tab:
        if type(elem) is list:
            sum += rekFindUsed(elem)
        else:
            sum += elem
    return sum


def rekFindRet(tab):
    sum = 0
    for elem in tab:
        if type(elem) is list:
            sum += rekFindRet(elem)
        else:
            sum += elem

    if sum < ret[0] and sum >= requiredSpace:
        ret[0] = sum
    return sum


rekFunc(data, ind, tree, len(data))
freeSpace = allSpace - rekFindUsed(tree)
requiredSpace = neededSpace - freeSpace
rekFindRet(tree)

print(ret[0])

f.close()
