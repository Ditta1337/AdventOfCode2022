with open("./15/input.txt") as f:
    data = f.readlines()


def parseData():
    # (Xo, Yo, R)
    points = []
    for line in data:
        elems = line.split()
        centerX = int(elems[2].split("=")[1].replace(",", ""))
        centerY = int(elems[3].split("=")[1].replace(":", ""))
        beaconX = int(elems[8].split("=")[1].replace(",", ""))
        beaconY = int(elems[9].split("=")[1])
        distance = abs(centerX - beaconX) + abs(centerY - beaconY)
        points.append((centerX, centerY, distance))

    return points


def findIntervals(y):
    intervals = []
    points = parseData()

    for point in points:
        distanceY = abs(y - point[1])
        distanceX = point[2] - distanceY

        if distanceX >= 0:
            intervals.append((point[0] - distanceX, point[0] + distanceX))

    return intervals


def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged:
            merged.append(interval)
        else:
            last = merged[-1]
            if interval[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], interval[1]))
            else:
                merged.append(interval)

    return merged


def findOverlapsAndRet():
    ret = 0
    xMin = 0
    xMax = 4000000
    yMin = 0
    yMax = 4000000 #2601918
    flag = 0

    for y in range(yMax, yMin, -1):
        intervals = mergeIntervals(findIntervals(y))
        print(y)
        for i in range(len(intervals) - 1):
            if (
                intervals[i][1] >= xMin
                and intervals[i + 1][0] <= xMax
                and intervals[i][1] - intervals[i + 1][0] == -2
            ):
                ret = (intervals[i][1] + 1) * 4000000 + y
                flag = 1
        if flag == 1:
                break

    return ret


print(findOverlapsAndRet())

f.close()
