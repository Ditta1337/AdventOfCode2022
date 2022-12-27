with open("./23/input.txt") as f:
    data = f.readlines()


def getElves(data):
    elves = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                elves.append((y, x))

    return elves

def checkSides(elf, elves, directions):
    doNothingCounter = 0
    for direction in directions:
        for move in direction:
            if (elf[0] + move[0], elf[1] + move[1]) not in elves:
                doNothingCounter += 1

    if doNothingCounter == 12:
        return elf

    for ind, direction in enumerate(directions):
        if all((elf[0] + move[0], elf[1] + move[1]) not in elves for move in direction):
            nextPos = (elf[0] + directions[ind][0][0], elf[1] + directions[ind][0][1])
            return nextPos
    return elf

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
    elves = getElves(data)
    numOfElves = len(elves)

    i = 0
    while True:
        i += 1
        foundOnce = set()
        foundMoreTimes = set()
        countSettled = 0

        for elf in elves:
            nextPos = checkSides(elf, elves, directions)
            if nextPos == elf:
                countSettled += 1
                continue
            if nextPos in foundMoreTimes:
                pass
            elif nextPos in foundOnce:
                foundMoreTimes.add(nextPos)
            else:
                foundOnce.add(nextPos)

        elvesCpy = set(elves)

        for elf in elvesCpy:
            nextPos = checkSides(elf, elvesCpy, directions)
            if nextPos == elf:
                continue
            if nextPos not in foundMoreTimes:
                elves.remove(elf)
                elves.append(nextPos)

        print("How many settled:", countSettled, "All elves:", numOfElves)
    
        if countSettled == numOfElves:
            break

        directions.append(directions.pop(0))

    print("Empty spaces:", countEmptySpaces(elves))
    print("Num of rounds it took to spread:", i)


main()


f.close()
