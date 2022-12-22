with open('./03/input.txt') as f:
    data = f.readlines()

ret = 0
base = 26

for line in data:
    length = len(line) - 1
    tab = [0 for _ in range(2*base)]
    
    for i in range(length // 2):
        ind = ord(line[i])
        if ind < ord("a"):
            ind = ind - ord("A") + base
            tab[ind] += 1
        else:
            ind = ind - ord("a")
            tab[ind] += 1
    for i in range(length // 2, length):
        ind = ord(line[i])
        if ind < ord("a"):
            ind = ind - ord("A") + base
            if tab[ind] >= 1:
                ret += ind + 1
                break
        else:
            ind = ind - ord("a")
            if tab[ind] >= 1:
                ret += ind + 1
                break    


print(ret)
f.close()
