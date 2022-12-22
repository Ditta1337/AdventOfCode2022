with open('./09/input.txt') as f:
    data = f.readlines()

ret = set()
h = [0, 0]
t = [0, 0]


def checkT():
    vec_x = h[0] - t[0]
    vec_y = h[1] - t[1]
    if vec_x == 2 and vec_y == 0:
        t[0] += 1
    elif vec_x == -2 and vec_y == 0:
        t[0] -= 1
    elif vec_x == 0 and vec_y == 2:
        t[1] += 1
    elif vec_x == 0 and vec_y == -2:
        t[1] -= 1
    elif vec_x > 0 and vec_y > 0 and (vec_x == 2 or vec_y == 2):
        t[0] += 1
        t[1] += 1
    elif vec_x > 0 and vec_y < 0 and (vec_x == 2 or vec_y == -2):
        t[0] += 1
        t[1] -= 1
    elif vec_x < 0 and vec_y > 0 and (vec_x == -2 or vec_y == 2):
        t[0] -= 1
        t[1] += 1
    elif vec_x < 0 and vec_y < 0 and (vec_x == -2 or vec_y == -2):
        t[0] -= 1
        t[1] -= 1


for line in data:
    move = line.split()
    ret.add(tuple(t))
    for _ in range(int(move[1])):
        match move[0]:
            case 'R':
                h[0] += 1
            case 'L':
                h[0] -= 1
            case 'U':
                h[1] += 1
            case 'D':
                h[1] -= 1
        checkT()
        ret.add(tuple(t))

print(len(ret))

f.close()
