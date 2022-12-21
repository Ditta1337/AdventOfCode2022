import re

with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/19/input.txt") as f:
    data = f.readlines()


def parseData(data):
    resourcesDict = {"ore": 0, "clay": 1, "obsidian": 2}
    blueprints = []
    for line in data:
        resourcesMax = [0 for _ in range(3)]
        blueprint = []
        for elems in line.split(": ")[1].split(". "):
            for number, ingridient in re.findall(r"(\d+) (\w+)", elems):
                index = resourcesDict[ingridient]
                blueprint.append(int(number))
                resourcesMax[index] = max(resourcesMax[index], int(number))

        blueprints.append((blueprint, resourcesMax))

    return blueprints


def dfs():

    def dfsRek(
        time,
        botKind,
        oreBots,
        clayBots,
        obsidianBots,
        geodeBots,
        ore,
        clay,
        obsidian,
        geode,
    ):
        nonlocal oreBot0, clayBot0, obsidianBot0, obsidianBot1, geodeBot0, geodeBot3
        nonlocal oreMax, clayMax, obsidianMax
        nonlocal foundGeodes, geodesToGain

        if (
            botKind == 0 and oreBots >= oreMax or
            botKind == 1 and clayBots >= clayMax or
            botKind == 2 and (obsidianBots >= obsidianMax or clayBots == 0) or
            # we dont check for oreBots == 0, because it is never true
            botKind == 3 and obsidianBots == 0 or
            # geodes + geodes to gain with bots we have + geodes to gain in Best Case
            geode + time * geodeBots + geodesToGain[time] <= foundGeodes
        ):

            return

        while time:

            if botKind == 0 and ore >= oreBot0:
                for newBotKind in range(4):
                    dfsRek(
                        time - 1,
                        newBotKind,
                        oreBots + 1,
                        clayBots,
                        obsidianBots,
                        geodeBots,
                        ore - oreBot0 + oreBots,
                        clay + clayBots,
                        obsidian + obsidianBots,
                        geode + geodeBots,
                    )
                return
            
            elif botKind == 1 and ore >= clayBot0:
                for newBotKind in range(4):
                    dfsRek(
                        time - 1,
                        newBotKind,
                        oreBots,
                        clayBots + 1,
                        obsidianBots,
                        geodeBots,
                        ore - clayBot0 + oreBots,
                        clay + clayBots,
                        obsidian + obsidianBots,
                        geode + geodeBots,
                    )
                return
            
            elif botKind == 2 and ore >= obsidianBot0 and clay >= obsidianBot1:
                for newBotKind in range(4):
                    dfsRek(
                        time - 1,
                        newBotKind,
                        oreBots,
                        clayBots,
                        obsidianBots + 1,
                        geodeBots,
                        ore - obsidianBot0 + oreBots,
                        clay - obsidianBot1 + clayBots,
                        obsidian + obsidianBots,
                        geode + geodeBots,
                    )
                return

            elif botKind == 3 and ore >= geodeBot0 and obsidian >= geodeBot3:
                for newBotKind in range(4):
                    dfsRek(
                        time - 1,
                        newBotKind,
                        oreBots,
                        clayBots,
                        obsidianBots,
                        geodeBots + 1,
                        ore - geodeBot0 + oreBots,
                        clay + clayBots,
                        obsidian - geodeBot3 + obsidianBots,
                        geode + geodeBots,
                    )
                return
            
            time -= 1
            ore += oreBots
            clay += clayBots
            obsidian += obsidianBots
            geode += geodeBots

         
        foundGeodes = max(foundGeodes, geode)


    # Best Case: fron now on for the rest of time you build geodeBots
    #   t
    #   Σ(i - 1) = (n - 1) * t // 2
    # i = 0
    # where t is left time, (i - 1), because you cant dig geode with freshy build bot
    bluepritns = parseData(data)
    time = 24
    geodesToGain = [(t - 1) * t // 2 for t in range(24 + 1)]
    ret = 1
    bpNum = 1

    for bp, maxes in bluepritns:
        oreBot0, clayBot0, obsidianBot0, obsidianBot1, geodeBot0, geodeBot3 = bp
        oreMax, clayMax, obsidianMax = maxes
        foundGeodes = 0
        for botKind in range(4):
            oreBots, clayBots, obsidianBots, geodeBots = 1, 0, 0, 0
            ore, clay, obsidian, geode = 0, 0, 0, 0
            dfsRek(
                time,
                botKind,
                oreBots,
                clayBots,
                obsidianBots,
                geodeBots,
                ore,
                clay,
                obsidian,
                geode,
            )
        ret += foundGeodes * bpNum
        bpNum += 1

    print(ret)  

dfs()

f.close()
