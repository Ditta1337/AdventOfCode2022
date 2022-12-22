with open("./14/input.txt") as f:
    data = f.readlines()


def findBoundriesAndLines():
    bottom = 0
    allLines = []

    for line in data:
        elems = line.replace("\n", "").split("->")
        lines = []
        for elem in elems:
            point = elem.split(",")
            point[0] = int(point[0])
            point[1] = int(point[1])
            lines.append(point)
            bottom = max(bottom, point[1])
        allLines.append(lines)
    return bottom + 3, allLines


def makeCave():
    bottom, allLines = findBoundriesAndLines()
    right = 500 + bottom
    cave = [[" " for _ in range(right)] for _ in range(bottom)]

    for line in allLines:
        for i in range(len(line) - 1):
            pointA = line[i]
            pointB = line[i + 1]
            path = [pointA[0] - pointB[0], pointA[1] - pointB[1]]
            if path[0] == 0:
                for i in range(abs(path[1]) + 1):
                    if path[1] < 0:
                        cave[pointA[1] + i][pointA[0]] = "#"
                    else:
                        cave[pointA[1] - i][pointA[0]] = "#"
            else:
                for i in range(abs(path[0]) + 1):
                    if path[0] < 0:
                        cave[pointA[1]][pointA[0] + i] = "#"
                    else:
                        cave[pointA[1]][pointA[0] - i] = "#"

    for i in range(right):
        cave[bottom - 1][i] = "#"

    return cave, bottom


# Could easly be done without recursion, but I wanted to try it out
# recursion slowes it down a LOT
def moveSand(sandPos, cave, bottom):
    if cave[sandPos[1] + 1][sandPos[0]] == " ":
        sandPos[1] += 1
        return moveSand(sandPos, cave, bottom)
    elif cave[sandPos[1] + 1][sandPos[0] - 1] == " ":
        sandPos[1] += 1
        sandPos[0] -= 1
        return moveSand(sandPos, cave, bottom)
    elif cave[sandPos[1] + 1][sandPos[0] + 1] == " ":
        sandPos[1] += 1
        sandPos[0] += 1
        return moveSand(sandPos, cave, bottom)
    elif sandPos[1] == 0:
        return False
    else:
        cave[sandPos[1]][sandPos[0]] = "o"
        return True


def dropSand():
    ret = 0
    sandPos = [500, 0]
    cave, bottom = makeCave()

    while moveSand(sandPos, cave, bottom):
        ret += 1
        sandPos = [500, 0]

    print("Sand placed: ", ret + 1)


dropSand()

f.close()
