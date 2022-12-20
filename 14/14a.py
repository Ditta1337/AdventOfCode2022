import time
import os

with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/14/input.txt") as f:
    data = f.readlines()


def findBoundriesAndLines():
    right = 0
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
            right = max(right, point[0])
            bottom = max(bottom, point[1])
        allLines.append(lines)

    return bottom, right, allLines


def makeCave():
    bottom, right, allLines = findBoundriesAndLines()
    cave = [[" " for _ in range(right + 2)] for _ in range(bottom + 2)]

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

    return cave, bottom


def printCave(cave, printY):
    for line in cave[printY : printY + 30]:
        for elem in line[450:550]:
            print(elem, end="")
        print()
    time.sleep(0.05)
    os.system("clear")


def moveSand(sandPos, cave, bottom):
    if sandPos[1] == bottom:
        return False

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
    else:
        cave[sandPos[1]][sandPos[0]] = "o"
        return True


def dropSand():
    ret = 0
    lowest = 0
    sandPos = [500, 0]
    cave, bottom = makeCave()

    while moveSand(sandPos, cave, bottom):
        ret += 1
        if sandPos[1] - 25 > lowest:
            lowest = sandPos[1] - 25
        printCave(cave, lowest)
        sandPos = [500, 0]

    print("Sand placed: ", ret)


dropSand()

f.close()
