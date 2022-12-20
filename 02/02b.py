with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/02/input.txt') as f:
    data = f.readlines()

ret = 0

for line in data:
    enemy = line[0]
    me = line[2]
    
    #X Y Z
    #A B C

    match enemy:                 
        case "A":
            if me == "X":
                ret += 3
            elif me == "Y":
                ret += 3 + 1
            else:
                ret += 6 + 2
        case "B":
            if me == "X":
                ret += 1
            elif me == "Y":
                ret += 3 + 2
            else:
                ret += 6 + 3
        case "C":
            if me == "X":
                ret += 2
            elif me == "Y":
                ret += 3 + 3
            else:
                ret += 6 + 1

print(ret)
f.close()