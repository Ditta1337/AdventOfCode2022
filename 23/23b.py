with open("./23/input.txt") as f:
    data = f.readlines()


def getElves(data):
    elves = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                elves.append((y, x))

    return elves


# it is slow as fuck, but works
def checkSides(elf, elves, direction, directions):
    newDirection = -1
    doNothingCounter = 0
    flag = 0
    for i in range(4):
        counter = 0
        for checkPos in directions[(direction + i) % 4]:
            if (elf[0] + checkPos[0], elf[1] + checkPos[1]) in elves:
                break
            counter += 1
            doNothingCounter += 1
        if counter == 3 and flag == 0:
            newDirection = directions[(direction + i) % 4][0]
            flag = 1

    if doNothingCounter == 12 or newDirection == -1:
        return elf

    nextPos = (elf[0] + newDirection[0], elf[1] + newDirection[1])
    return nextPos


def filterMoves(wantedMoves, moves):
    moves = list(filter(lambda x: moves.count(x) == 1, moves))
    tmpTab = []
    for move in moves:
        for elem in wantedMoves:
            if elem[0] == move:
                tmpTab.append(elem)
                break
    wantedMoves = tmpTab

    return wantedMoves


def countEmptySpaces(elves):
    elvesToPrint = []
    minX, minY, maxX, maxY = 9**9, 9**9, -(9**9), -(9**9)

    for elf in elves:
        if elf[0] > maxY:
            maxY = elf[0]
        if elf[0] < minY:
            minY = elf[0]
        if elf[1] > maxX:
            maxX = elf[1]
        if elf[1] < minX:
            minX = elf[1]

    for elf in elves:
        elvesToPrint.append((elf[0] + abs(minY), elf[1] + abs(minX)))

    # print visualization
    printField(elvesToPrint, maxY + abs(minY) + 1, maxX + abs(minX) + 1)

    field = (maxX - minX + 1) * (maxY - minY + 1)

    return field - len(elves)


def printField(elvesToPrint, height, width):
    field = [[" " for _ in range(width)] for _ in range(height)]

    for elf in elvesToPrint:
        field[elf[0]][elf[1]] = "#"

    for line in field:
        for char in line:
            print(char, end="")
        print()


def main():
    #               N, S, W, E
    directions = [
        [(-1, 0), (-1, -1), (-1, 1)],
        [(1, 0), (1, -1), (1, 1)],
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (1, 1), (-1, 1)],
    ]
    direction = 0
    elves = getElves(data)
    numOfElves = len(elves)
    roundsCounter = 0

    while True:
        roundsCounter += 1
        wantedMoves = []
        moves = []
        endCounter = 0
        for elf in elves:
            newPos = checkSides(elf, elves, direction, directions)
            if elf == newPos:
                endCounter += 1
            else:
                wantedMoves.append((newPos, elf))
                moves.append(newPos)

        if endCounter == numOfElves:
            break

        # filtered wanted moves to same position
        wantedMoves = filterMoves(wantedMoves, moves)

        for ind, elf in enumerate(elves):
            for move in wantedMoves:
                if move[1] == elf:
                    elves[ind] = move[0]

        direction = (direction + 1) % 4
        print("Settled:", endCounter, "All Elves:", numOfElves)

    print(roundsCounter)


main()


f.close()
