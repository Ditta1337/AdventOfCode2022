import re

with open("./21/input.txt") as f:
    data = f.readlines()


def findLine(data, toFind):
    pattern = re.compile(r"^" + re.escape(toFind))
    for line in data:
        if pattern.match(line):
            return line


def rekFindEquation(line, data, equation):
    elems = line.split()
    if len(elems) == 2:
        equation[0] += elems[1]
        return
    else:
        equation[0] += "("
        rekFindEquation(findLine(data, elems[1]), data, equation)
        equation[0] += elems[2]
        rekFindEquation(findLine(data, elems[3]), data, equation)
        equation[0] += ")"


def main():
    equation = [""]
    rekFindEquation(findLine(data, "root:"), data, equation)
    # I am aware of the eval() security issues
    ret = int(eval(equation[0]))
    print(ret)


main()


f.close()
