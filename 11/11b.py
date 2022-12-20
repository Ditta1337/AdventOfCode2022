with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/11/input.txt") as f:
    data = f.readlines()

ret = 1
rounds = 10000
monkeys = []


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ""
        self.test = 0
        self.test_true = 0
        self.test_false = 0
        self.moves = 0


def parseData(data):
    currInd = -1

    for line in data:
        elems = line.split()

        if elems == []:
            continue

        match elems[0]:
            case "Monkey":
                currInd += 1
                monkey = Monkey()
                monkeys.append(monkey)
            case "Starting":
                monkeys[currInd].items = list(
                    map(int, [i.split(",")[0] for i in elems[2:]])
                )
            case "Operation:":
                monkeys[currInd].operation = elems[-2] + " " + elems[-1]
            case "Test:":
                monkeys[currInd].test = int(elems[-1])
            case "If":
                if elems[1] == "true:":
                    monkeys[currInd].test_true = int(elems[-1])
                else:
                    monkeys[currInd].test_false = int(elems[-1])


def findCommonDivisor(monkeys):
    ret = 1
    for monkey in monkeys:
        ret *= monkey.test
    return ret


def returnRet(data):
    parseData(data)
    commonDivisor = findCommonDivisor(monkeys)

    moves = []

    for i in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)

                if monkey.operation[2] == "o":
                    k = item
                else:
                    k = int(monkey.operation.split(" ")[1])
                if monkey.operation[0] == "*":
                    item = item * k
                else:
                    item = item + k

                if item > commonDivisor:
                    item = item % commonDivisor

                if item % monkey.test == 0:
                    monkeys[monkey.test_true].items.append(item)
                else:
                    monkeys[monkey.test_false].items.append(item)

                monkey.moves += 1

            if i == rounds - 1:
                moves.append(monkey.moves)
            
    moves.sort()
    return moves[-1] * moves[-2]


print(returnRet(data))

f.close()
