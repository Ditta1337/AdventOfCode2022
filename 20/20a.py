with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/20/input.txt") as f:
    data = f.readlines()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def createLinkedList(data):
    linkedList = [Node(int(line)) for line in data]

    for i in range(len(linkedList)):
        linkedList[i].next = linkedList[(i + 1) % len(linkedList)]
        linkedList[i].prev = linkedList[(i - 1) % len(linkedList)]

    return linkedList


def mix(linkedList):

    divisor = len(linkedList) - 1

    for node in linkedList:
        if node.value == 0:
            zeroNode = node
            continue

        newNeighbour = node

        if node.value > 0:
            for _ in range(node.value % divisor):
                newNeighbour = newNeighbour.next

        else:
            for _ in range((-node.value) % divisor + 1):
                newNeighbour = newNeighbour.prev

        if newNeighbour == node:
            continue

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = newNeighbour
        node.next = newNeighbour.next
        newNeighbour.next.prev = node
        newNeighbour.next = node

    return zeroNode


def decrypt(zeroNode):
    ret = 0
    for _ in range(3):
        for _ in range(1000):
            zeroNode = zeroNode.next
        ret += zeroNode.value
    print(ret)


def main():
    linkedList = createLinkedList(data)
    zeroNode = mix(linkedList)
    decrypt(zeroNode)


main()

f.close()