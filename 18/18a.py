with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/18/input.txt") as f:
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


def main():
    ret = 0
    cubes = []
    
    for line in data:
        elems = line.split(",")
        cube = (int(elems[0]), int(elems[1]), int(elems[2]))
        ret += addCube(cube, cubes)

    print(ret)


main()

f.close()
