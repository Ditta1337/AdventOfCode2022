import ast

with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/13/input.txt") as f:
    data = f.readlines()


def checkTab(left, right):
    length = min(len(left), len(right))
    check = None
    for i in range(length):
        leftType = type(left[i])
        rightType = type(right[i])
        if leftType == list and rightType == list:
            check = checkTab(left[i], right[i])
            if check != None:
                return check
        if leftType == int and rightType == int:
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
        if leftType == int and rightType == list:
            check = checkTab([left[i]], right[i])
            if check != None:
                return check
        if leftType == list and rightType == int:
            check = checkTab(left[i], [right[i]])
            if check != None:
                return check

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False


def addAllPackets(tab):
    for line in data:
        if line != "\n":
            tab.append(ast.literal_eval(line))


def sortAllPackets():
    tab = [[[2]], [[6]]]
    addAllPackets(tab)
    length = len(tab)

    for i in range(length):
        for j in range(0, length - i - 1):
            if not checkTab(tab[j], tab[j + 1]):
                tab[j], tab[j + 1] = tab[j + 1], tab[j]

    return (tab.index([[2]]) + 1) * (tab.index([[6]]) + 1)


print(sortAllPackets())

f.close()
