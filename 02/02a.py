with open('./02/input.txt') as f:
    data = f.readlines()

ret = 0

for line in data:
    enemy = line[0]
    me = line[2]
    
    #X Y Z
    #A B C

    match enemy:                 
        case "A":
            if me == "Y":
                ret += 6 + 2
            elif me == "X":
                ret += 3 + 1
            else:
                ret += 3
        case "B":
            if me == "Z":
                ret += 6 + 3
            elif me == "Y":
                ret += 3 + 2
            else:
                ret += 1
        case "C":
            if me == "X":
                ret += 6 + 1
            elif me == "Z":
                ret += 3 + 3
            else:
                ret += 2

print(ret)
f.close()