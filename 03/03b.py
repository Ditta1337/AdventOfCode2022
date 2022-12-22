with open('./03/input.txt') as f:
    data = f.readlines()

ret = 0
base = 26
counter = 0

for line in data:
    if counter % 3 == 0:
        tab = [[] for _ in range(2*base)]

    length = len(line) - 1
    for i in range(length):
        ind = ord(line[i])
        if ind < ord("a"):
            ind = ind - ord("A") + base
            if str(counter%3) not in tab[ind]:
                tab[ind].append(str(counter%3))
        else:
            ind = ind - ord("a")
        if str(counter%3) not in tab[ind]:
                tab[ind].append(str(counter%3))
    counter += 1
    if counter % 3 == 0:
        for ind, elem in enumerate(tab):
            if len(elem) == 3:
                ret += ind + 1
        

print(ret)
f.close()
