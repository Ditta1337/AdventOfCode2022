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
        length = len(line)
        mapLength = max(mapLength, len(line))

    # adding padding to map so I dont have to check for out of bounds
    mapHeight += 2
    mapLength += 1  # +1 because \n has its own width

    instructionIndex = mapHeight
    instructions = re.findall(
        r"(?=[0-9])[0-9]*|(?=[A-Z])[A-Z]*", data[instructionIndex - 1]
    )

    adventureMap = [[" " for _ in range(mapLength)] for _ in range(mapHeight)]

    # fill map
    for i in range(mapHeight - 1):
        for j in range(len(data[i]) - 1):
            toAdd = data[i][j]
            if toAdd == "\n":
                toAdd = " "
            adventureMap[i + 1][j + 1] = toAdd

    return adventureMap, instructions


def moveSides(position, direction):
    # hard coded because I'm not an algebra god
    y, x = position
    if y == 0 and 51 <= x < 101 and direction == (-1, 0):
        direction = (0, 1)
        y, x = x + 100, 1
    elif x == 0 and 151 <= y < 201 and direction == (0, -1):
        direction = (1, 0)
        y, x = 1, y - 100
    elif y == 0 and 101 <= x < 151 and direction == (-1, 0):
        y, x = 200, x - 100
    elif y == 201 and 1 <= x < 51 and direction == (1, 0):
        y, x = 1, x + 100
    elif x == 151 and 1 <= y < 51 and direction == (0, 1):  #!!!
        direction = (0, -1)
        y, x = 151 - y, 100
    elif x == 101 and 101 <= y < 151 and direction == (0, 1):  #!!!
        direction = (0, -1)
        y, x = 151 - y, 150
    elif x == 50 and 1 <= y < 51 and direction == (0, -1):  # !!!
        direction = (0, 1)
        y, x = 151 - y, 1
    elif x == 0 and 101 <= y < 151 and direction == (0, -1):  # !!!
        direction = (0, 1)
        y, x = 151 - y, 51
    elif y == 51 and 101 <= x < 151 and direction == (1, 0):
        direction = (0, -1)
        y, x = x - 50, 100
    elif x == 101 and 51 <= y < 101 and direction == (0, 1):
        direction = (-1, 0)
        y, x = 50, y + 50
    elif y == 151 and 51 <= x < 101 and direction == (1, 0):
        direction = (0, -1)
        y, x = x + 100, 50
    elif x == 51 and 151 <= y < 201 and direction == (0, 1):
        direction = (-1, 0)
        y, x = 150, y - 100
    elif y == 100 and 1 <= x < 51 and direction == (-1, 0):
        direction = (0, 1)
        y, x = x + 50, 51
    elif x == 50 and 51 <= y < 101 and direction == (0, -1):
        direction = (1, 0)
        y, x = 101, y - 50

    return (y, x), direction


def isBlocked(adventureMap, position, direction):
    nextPos = (position[0] + direction[0], position[1] + direction[1])
    newDirection = direction
    if adventureMap[nextPos[0]][nextPos[1]] == " ":
        nextPos, newDirection = moveSides(nextPos, direction)
    if adventureMap[nextPos[0]][nextPos[1]] == "#":
        return position, direction  # blocked
    return nextPos, newDirection  # not blocked


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
                position, newDirection = isBlocked(
                    adventureMap, position, directions[direction]
                )
                direction = directions.index(newDirection)

    adventureMap[position[0]][position[1]] = "📍"

    # print adventure map
    for line in adventureMap:
        for char in line:
            print(char, end="")
        print()

    print(position[0] * 1000 + position[1] * 4 + direction)


main()

f.close()