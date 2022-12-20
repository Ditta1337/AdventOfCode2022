with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/09/input.txt') as f:
    data = f.readlines()

ret = set()
knots = [[0, 0] for _ in range(10)]


def checkKnot(knot, lastKnot):
    vec_x = lastKnot[0] - knot[0]
    vec_y = lastKnot[1] - knot[1]
    if vec_x == 2 and vec_y == 0:
        knot[0] += 1
    elif vec_x == -2 and vec_y == 0:
        knot[0] -= 1
    elif vec_x == 0 and vec_y == 2:
        knot[1] += 1
    elif vec_x == 0 and vec_y == -2:
        knot[1] -= 1
    elif vec_x > 0 and vec_y > 0 and (vec_x == 2 or vec_y == 2):
        knot[0] += 1
        knot[1] += 1
    elif vec_x > 0 and vec_y < 0 and (vec_x == 2 or vec_y == -2):
        knot[0] += 1
        knot[1] -= 1
    elif vec_x < 0 and vec_y > 0 and (vec_x == -2 or vec_y == 2):
        knot[0] -= 1
        knot[1] += 1
    elif vec_x < 0 and vec_y < 0 and (vec_x == -2 or vec_y == -2):
        knot[0] -= 1
        knot[1] -= 1


ret.add(tuple(knots[0]))
for line in data:
    move = line.split()
    for _ in range(int(move[1])):
        match move[0]:
            case 'R':
                knots[0][0] += 1
            case 'L':
                knots[0][0] -= 1
            case 'U':
                knots[0][1] += 1
            case 'D':
                knots[0][1] -= 1
        for i in range(1, len(knots), 1):
            checkKnot(knots[i], knots[i - 1])
        ret.add(tuple(knots[len(knots) - 1]))

print(len(ret))

f.close()
