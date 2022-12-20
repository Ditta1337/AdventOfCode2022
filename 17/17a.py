with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/17/input.txt") as f:
    data = f.readlines()


def addObject(clock, screen, height):
    ret = []
    objectHeight = 0
    match clock % 5:
        case 0:  # dash
            ret = [[0, 2], [0, 3], [0, 4], [0, 5]]
            objectHeight = 1
        case 1:  # cross
            ret = [[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]]
            objectHeight = 3
        case 2:  # reverse L
            ret = [[0, 4], [1, 4], [2, 4], [2, 3], [2, 2]]
            objectHeight = 3
        case 3:  # I
            ret = [[0, 2], [1, 2], [2, 2], [3, 2]]
            objectHeight = 4
        case 4:  # square
            ret = [[0, 2], [0, 3], [1, 2], [1, 3]]
            objectHeight = 2

    toAdd = objectHeight - height + 3
    if toAdd > 0:
        for _ in range(objectHeight - height + 3):
            screen.insert(0, [" ", " ", " ", " ", " ", " ", " "])
    else:
        for _ in range(abs(toAdd)):
            screen.pop(0)
    return ret


def printScreen(screen):
    for line in screen:
        print(line)


def moveRight(screen, position):
    canMove = True
    for pos in position:
        if pos[1] == len(screen[0]) - 1 or screen[pos[0]][pos[1] + 1] == "#":
            canMove = False

    if canMove:
        for pos in position:
            pos[1] += 1


def moveLeft(screen, position):
    canMove = True
    for pos in position:
        if pos[1] == 0 or screen[pos[0]][pos[1] - 1] == "#":
            canMove = False

    if canMove:
        for pos in position:
            pos[1] -= 1


def moveDown(screen, position):
    for pos in position:
        if pos[0] == len(screen) - 1 or screen[pos[0] + 1][pos[1]] == "#":
            return True

    for pos in position:
        pos[0] += 1
    return False


def deleteScreen(screen):

    for ind, line in enumerate(screen):
        canDelete = True
        for tile in line:
            if tile != "#":
                canDelete = False
        if canDelete:
            ret = len(screen) - ind
            for i in range(len(screen) - ind):
                screen.pop(ind)
            return ret
    return 0


def addToScreen(screen, position):
    for pos in position:
        screen[pos[0]][pos[1]] = "#"


def maintainScreen(screen):
    for ind, line in enumerate(screen):
        for tile in line:
            if tile == "#":
                return ind
    return 0


def findHighestPosition(screen):
    return len(screen) - maintainScreen(screen)


def main():
    rocksToFall = 2022
    screen = []
    moves = data[0]
    ret = 0
    clock = 0
    rocks = 0
    while True:
        position = addObject(rocks, screen, maintainScreen(screen))
        rocks += 1
        isPlaced = False
        while not isPlaced:
            if moves[clock] == ">":
                moveRight(screen, position)
            elif moves[clock] == "<":
                moveLeft(screen, position)
            isPlaced = moveDown(screen, position)
            if clock == len(moves) - 1:
                clock = -1
            clock += 1
        ret += deleteScreen(screen)

        addToScreen(screen, position)
        if rocks == rocksToFall:
            printScreen(screen)
            ret += findHighestPosition(screen)
            break

    print("Height if", rocksToFall, "rocks fallen:", ret)


main()

f.close()
