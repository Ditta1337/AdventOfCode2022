with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/08/input.txt') as f:
    data = f.readlines()

ret = set()


def fromLeft(data):
    for index_y, line in enumerate(data):
        lowest = -1
        for index_x, height in enumerate(line):
            if height != '\n':
                height = int(height)
                if height > lowest:
                    ret.add((index_x, index_y))
                    lowest = height


def fromRight(data):
    for index_y, line in enumerate(data):
        lowest = -1
        length = len(line)
        for index_x in range(length - 1, -1, -1):
            if line[index_x] != '\n':
                height = int(line[index_x])
                if height > lowest:
                    ret.add((index_x, index_y))
                    lowest = height


def formTop(data):
    length = len(data[0])
    for index_x in range(length - 1):
        lowest = -1
        for index_y, line in enumerate(data):
            height = int(line[index_x])
            if height > lowest:
                ret.add((index_x, index_y))
                lowest = height


def fromBottom(data):
    lenght = len(data[0])
    numOfLines = len(data)
    for index_x in range(lenght - 1):
        lowest = -1
        for index_y in range(numOfLines - 1, -1, -1):
            height = int(data[index_y][index_x])
            if height > lowest:
                ret.add((index_x, index_y))
                lowest = height


fromLeft(data)
fromRight(data)
formTop(data)
fromBottom(data)
print(len(ret))

f.close()
