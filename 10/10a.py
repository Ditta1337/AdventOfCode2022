with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/10/input.txt') as f:
    data = f.readlines()

register = 1
clock = 0
ret = [0]



def checkIndex(clock, register):
    if (clock + 20) % 40 == 0:
        ret[0] += register * clock


for line in data:
    elems = line.split()
    match elems[0]:
        case 'noop':
            clock += 1
            checkIndex(clock, register)
            continue
        case 'addx':
            for i in range(2):
                clock += 1
                checkIndex(clock, register)
            register += int(elems[1])

print(ret[0])

f.close()
