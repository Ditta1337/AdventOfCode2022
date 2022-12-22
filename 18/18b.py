from collections import deque

with open("./18/input.txt") as f:
    data = f.readlines()


def addCube(newCube, cubes):
    toAdd = 6
    for cube in cubes:
        if newCube[0] == cube[0] and newCube[1] == cube[1]:
            if newCube[2] == cube[2] + 1 or newCube[2] == cube[2] - 1:
                toAdd -= 2
        if newCube[0] == cube[0] and newCube[2] == cube[2]:
            if newCube[1] == cube[1] + 1 or newCube[1] == cube[1] - 1:
                toAdd -= 2
        if newCube[1] == cube[1] and newCube[2] == cube[2]:
            if newCube[0] == cube[0] + 1 or newCube[0] == cube[0] - 1:
                toAdd -= 2

    cubes.append(newCube)

    return toAdd


def findBox(cubes):
    maxX = 0
    maxY = 0
    maxZ = 0
    for cube in cubes:
        maxX = max(maxX, cube[0])
        maxY = max(maxY, cube[1])
        maxZ = max(maxZ, cube[2])

    #               + 1 because findAirPockets will think that there are bubbles
    #               in the corners of the box. This is like adding a padding of 1
    return -1, -1, -1, maxX + 1, maxY + 1, maxZ + 1


def findAirPockets(cubes, box, minX, minY, minZ, maxX, maxY, maxZ):
    pockets = set()
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            for z in range(minZ, maxZ):
                if (x, y, z) not in cubes and (x, y, z) not in box:
                    pockets.add((x, y, z))

    return pockets


def bfs3D(cubes, minX, minY, minZ, maxX, maxY, maxZ):
    box = []
    moves = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    start = (minX, minY, minZ)
    queue = deque()
    box.append(start)
    queue.append(start)
    while queue:
        pos = queue.popleft()
        # print(pos)
        for move in moves:
            newPos = (pos[0] + move[0], pos[1] + move[1], pos[2] + move[2])
            if (
                newPos not in box
                and newPos not in cubes
                and newPos[0] <= maxX
                and newPos[1] <= maxY
                and newPos[2] <= maxZ
                and newPos[0] >= minX
                and newPos[1] >= minY
                and newPos[2] >= minZ
            ):
                box.append(newPos)
                queue.append(newPos)

    return box


def main():
    ret = 0
    wholeArea = 0
    insideArea = 0
    cubes = []
    insideCubes = []

    for line in data:
        elems = line.split(",")
        cube = (int(elems[0]), int(elems[1]), int(elems[2]))
        wholeArea += addCube(cube, cubes)

    minX, minY, minZ, maxX, maxY, maxZ = findBox(cubes)
    box = bfs3D(cubes, minX, minY, minZ, maxX, maxY, maxZ)
    pockets = findAirPockets(cubes, box, minX, minY, minZ, maxX, maxY, maxZ)

    for pocket in pockets:
        insideArea += addCube(pocket, insideCubes)

    ret = wholeArea - insideArea

    print(ret)


main()

f.close()
