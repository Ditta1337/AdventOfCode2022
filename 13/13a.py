import ast

with open("./13/input.txt") as f:
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


def findValidPackets():
    ret = 0
    index = 1
    left = []
    right = []

    for ind, line in enumerate(data):
        if ind % 3 == 0:
            left = ast.literal_eval(line)
        elif (ind + 2) % 3 == 0:
            right = ast.literal_eval(line)
        if (ind + 4) % 3 == 0:
            if checkTab(left, right):
                ret += index
            index += 1
            left = []
            right = []

    return ret


print(findValidPackets())

f.close()
