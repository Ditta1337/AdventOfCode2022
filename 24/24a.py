from collections import deque

with open("./24/input.txt") as f:
    data = f.readlines()


def parseData(data):
    start = (0, 0)
    end = (0, 0)
    blizzards = []
    xMax = len(data[0]) - 2  # because \n
    yMax = len(data) - 1

    for ind, elem in enumerate(data[0]):  # x, y
        if elem == ".":
            start = (ind, 0)
    for ind, elem in enumerate(data[len(data) - 1]):
        if elem == ".":
            end = (ind, len(data) - 1)

    for y in range(len(data)):
        blizzard = -1
        for x, elem in enumerate(data[y]):
            if elem == "^":
                blizzard = (0, -1)
            elif elem == ">":
                blizzard = (1, 0)
            elif elem == "v":
                blizzard = (0, 1)
            elif elem == "<":
                blizzard = (-1, 0)
            if blizzard != -1:
                blizzards.append((x, y, blizzard))
                blizzard = -1

    return start, end, xMax, yMax, blizzards


def moveBlizzards(blizzards, xMax, yMax, blizzardsDict, pos):
    # xMax = 7, yMax = 5
    for ind, blizzard in enumerate(blizzards):
        nextX = blizzard[0] + blizzard[2][0]
        nextY = blizzard[1] + blizzard[2][1]

        if blizzard[2] == (0, -1) and nextY == 0:
            nextY = yMax - 1
        if blizzard[2] == (1, 0) and nextX == xMax:
            nextX = 1
        if blizzard[2] == (0, 1) and nextY == yMax:
            nextY = 1
        if blizzard[2] == (-1, 0) and nextX == 0:
            nextX = xMax - 1

        blizzards[ind] = (nextX, nextY, blizzard[2])

    printBlizzards(blizzards, xMax, yMax, blizzardsDict, pos)


def printBlizzards(blizzards, xMax, yMax, blizzardsDict, pos):
    for y in range(1, yMax):
        for x in range(1, xMax):
            if x == pos[0] and y == pos[1]:
                print("X", end="")
                continue
            printedFlag = 1
            for blizzard in blizzards:
                if x == blizzard[0] and y == blizzard[1]:
                    print(blizzardsDict[blizzard[2]], end="")
                    printedFlag = 0
                    break
            if printedFlag:
                print(".", end="")
        print()
    print()


def bfs(position, end, blizzards, xMax, yMax, blizzardsDict):
    moves = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    queue = deque()
    queue.append((position, 0, blizzards))
    breakCounter = 0
    retPath = []
    ret = 9**9

    while queue:
        pos, counter, poppedBlizzards = queue.popleft()
        breakCounter += 1
        if pos == end:
            return counter
        moveBlizzards(poppedBlizzards, xMax, yMax, blizzardsDict, pos)
        for move in moves:
            nextX = pos[0] + move[0]
            nextY = pos[1] + move[1]
            nextPos = (nextX, nextY)
            if (
                (
                    nextX > 0
                    and nextX < xMax
                    and nextY > 0
                    and nextY < yMax
                    and all(
                        (nextX, nextY) != (elem[0], elem[1]) for elem in poppedBlizzards
                    )
                )
                or nextPos == position
                or nextPos == end
            ):
                newBlizzards = poppedBlizzards[:]
                queue.append((nextPos, counter + 1, newBlizzards))

    return ret, retPath


def main():
    start, end, xMax, yMax, blizzards = parseData(data)
    blizzardsDict = {(0, -1): "^", (1, 0): ">", (0, 1): "v", (-1, 0): "<"}

    ret = bfs(start, end, blizzards, xMax, yMax, blizzardsDict)

    print(ret)


main()

f.close()
