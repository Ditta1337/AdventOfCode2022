with open('./07/input.txt') as f:
    data = f.readlines()

ret = [0]
ind = [0]
tree = []

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

def rekFindRet(tab):
    sum = 0
    for elem in tab:
        if type(elem) is list:
            sum += rekFindRet(elem)
        else:
            sum += elem
    if sum <= 100000:
        ret[0] += sum
    return sum

rekFunc(data, ind, tree, len(data))
rekFindRet(tree)

print(tree)

print(ret[0])

f.close()