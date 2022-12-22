import re

with open("./21/input.txt") as f:
    data = f.readlines()


def findLine(data, toFind):
    pattern = re.compile(r"^" + re.escape(toFind))
    for line in data:
        if pattern.match(line):
            return line


def rekFindEquation(line, data, equation, sideOfEq, startSide):
    elems = line.split()
    if len(elems) == 2:
        if elems[0] == "humn:":
            sideOfEq[0] = int(elems[1])
            equation[0] += "{}"
            return
        equation[0] += elems[1]
        return
    else:
        equation[0] += "("
        rekFindEquation(findLine(data, elems[1]), data, equation, sideOfEq, startSide)
        equation[0] += elems[2]
        rekFindEquation(findLine(data, elems[3]), data, equation, sideOfEq, startSide)
        equation[0] += ")"


def main():
    leftEquation = [f""]
    rightEquation = [f""]
    sideOfEq = [-1]
    line = findLine(data, "root:").split()
    rekFindEquation(findLine(data, line[1]), data, leftEquation, sideOfEq, 0)
    rekFindEquation(findLine(data, line[3]), data, rightEquation, sideOfEq, 1)

    humn = sideOfEq[0]

    left = int(eval(leftEquation[0].format(humn)))
    right = int(eval(rightEquation[0].format(humn)))
    diff0 = abs(left - right)

    diffCpy = diff0
    counter = 0

    while diffCpy > 0:
        counter += 1
        diffCpy //= 2

    toAdd = pow(2, counter)

    # binary search thingy
    while True:
        diff1 = diff0
        left = int(eval(leftEquation[0].format(humn)))
        right = int(eval(rightEquation[0].format(humn)))
        diff0 = abs(left - right)
        if diff0 == 0:
            break
        if diff0 > diff1:
            toAdd //= -2
        humn += toAdd

    left = int(eval(leftEquation[0].format(humn)))
    right = int(eval(rightEquation[0].format(humn)))

    print("Test:", left == right)
    print(humn)


main()


f.close()
