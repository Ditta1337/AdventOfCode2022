with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/16/input.txt") as f:
    data = f.readlines()

time = 30


def parseData():
    numOfNodes = len(data)
    nodesNames = []
    nodesDist = [[9**9 for _ in range(numOfNodes)] for _ in range(numOfNodes)]
    for i in range(numOfNodes):
        nodesDist[i][i] = 2
        nodesNames.append(data[i].split()[1])

    nodesFlow = []

    for line in data:
        flow = int(line.split()[4].split("=")[1].replace(";", ""))
        node = line.split()[1]
        nodeIndex = nodesNames.index(node)
        edges = line.split()[9:]
        for edge in edges:
            edgeName = edge.split(",")[0]
            edgeIndex = nodesNames.index(edgeName)
            nodesDist[nodeIndex][edgeIndex] = 1
            nodesDist[edgeIndex][nodeIndex] = 1
        nodesFlow.append(flow)

    return nodesFlow, nodesDist, numOfNodes, nodesNames


def floydWarshall(nodesDist, numOfNodes):

    for k in range(numOfNodes):
        for i in range(numOfNodes):
            for j in range(numOfNodes):
                nodesDist[i][j] = min(
                    nodesDist[i][j], nodesDist[i][k] + nodesDist[k][j]
                )

    return nodesDist


def rekFindScore(
    pos, time, visited, nodesDist, nodesFlows, bitwiseVisit, ret={}, score=0
):

    ret[visited] = max(ret.get(visited, 0), score)
    for newPos, node in enumerate(nodesDist):
        if nodesFlows[newPos] != 0:
            newTime = time - node[pos] - 1
            if time > 0 and not (
                visited & bitwiseVisit[newPos]
            ):  # if we have time and we didn't visit this node
                rekFindScore(
                    newPos,
                    newTime,
                    visited | bitwiseVisit[newPos],
                    nodesDist,
                    nodesFlows,
                    bitwiseVisit,
                    ret,
                    score + newTime * nodesFlows[newPos],
                )

    return ret


def findBestScore(t):
    nodesFlow, nodesDist, numOfNodes, nodesNames = parseData()
    nodesDist = floydWarshall(nodesDist, numOfNodes)
    bitwiseVisit = [1 << i for i in range(numOfNodes)]

    ret = max(
        rekFindScore(
            nodesNames.index("AA"), t, 0, nodesDist, nodesFlow, bitwiseVisit
        ).values()
    )

    print(ret)


findBestScore(time)

f.close()
