with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/15/input.txt") as f:
    data = f.readlines()

y = 2000000

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

def findIntervals():
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

    intervals = mergeIntervals(findIntervals())

    for interval in intervals:
        ret += interval[1] - interval[0]

    return ret


print(findOverlapsAndRet())

f.close()

