import re

with open("./22/input.txt") as f:
    data = f.readlines()


def parseData(data):
    mapHeight = 0
    mapLength = 0
    instructionIndex = 0
    adventureMap = []
    instructions = []

    for line in data:
        if line == "\n":
            break
        mapHeight += 1
        mapLength = max(mapLength, len(line))

    # adding padding to map so I dont have to check for out of bounds
    mapHeight += 2
    mapLength += 2

    instructionIndex = mapHeight
    instructions = re.findall(
        r"(?=[0-9])[0-9]*|(?=[A-Z])[A-Z]*", data[instructionIndex - 1]
    )

    adventureMap = [[" " for _ in range(mapLength)] for _ in range(mapHeight)]

    # fill map
    for i in range(mapHeight - 1):
        for j in range(len(data[i])):
            toAdd = data[i][j]
            if toAdd == "\n":
                toAdd = " "
            adventureMap[i + 1][j + 1] = toAdd

    return adventureMap, instructions


def wrap(adventureMap, position, direction):
    counterDirection = (-direction[0], -direction[1])
    nextPos = (position[0] + counterDirection[0], position[1] + counterDirection[1])

    while adventureMap[nextPos[0]][nextPos[1]] != " ":
        nextPos = (nextPos[0] + counterDirection[0], nextPos[1] + counterDirection[1])

    nextPos = (nextPos[0] + direction[0], nextPos[1] + direction[1])
    return nextPos


def isBlocked(adventureMap, position, direction):
    nextPos = (position[0] + direction[0], position[1] + direction[1])

    if adventureMap[nextPos[0]][nextPos[1]] == " ":
        nextPos = wrap(adventureMap, position, direction)
    if adventureMap[nextPos[0]][nextPos[1]] == "#":
        return position  # blocked
    return nextPos  # not blocked


def main():
    adventureMap, instructions = parseData(data)
    directionDict = {0: "→", 1: "↓", 2: "←", 3: "↑"}
    #              right   down     left     up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    position = (0, 0)
    direction = 0
    # find starting position
    for i in range(len(data[0])):
        if data[0][i] != " ":
            position = (1, i + 1)
            break

    for instruction in instructions:
        if instruction == "R":
            direction = (direction + 1) % 4
        elif instruction == "L":
            direction = (direction - 1) % 4
        else:
            for _ in range(int(instruction)):
                adventureMap[position[0]][position[1]] = directionDict[direction]
                position = isBlocked(adventureMap, position, directions[direction])

    adventureMap[position[0]][position[1]] = "📍"

    # print adventure map
    for line in adventureMap:
        for char in line:
            print(char, end="")
        print()

    print(position[0] * 1000 + position[1] * 4 + direction)


main()
