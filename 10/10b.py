with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/10/input.txt') as f:
    data = f.readlines()

register = 1
clock = 0
sprite = [1]


def returnCarier(clock):
    if clock % 40 == 0:
        print('\n')

def positionSprite(register):
    sprite[0] = register % 40


def draw(clock):
    pos = clock % 40
    if sprite[0] == pos or sprite[0] - 1 == pos or sprite[0] + 1 == pos:
        print('@ ', end='')
    else:
        print('  ', end='')


for line in data:
    elems = line.split()
    match elems[0]:
        case 'noop':
            draw(clock)
            clock += 1
            returnCarier(clock)
            continue
        case 'addx':
            for i in range(2):
                draw(clock)
                clock += 1
                returnCarier(clock)
            register += int(elems[1])
            positionSprite(register)

# REHPRLUB

f.close()
