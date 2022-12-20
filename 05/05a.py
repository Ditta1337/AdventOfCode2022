
with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/05/input.txt') as f:
    data = f.readlines()

ret = ""
stack = [[] for _ in range(9)]
flag = False
prev_flag = False
skip = 0


for line in data:
    if line[0] == " ":
        flag = True
        continue
    index = 0
    space_counter = -1
    tmp = ''
    info_tab = []
    for letter in line:
        if skip > 0:
            skip -= 1
            continue
        if not flag:
            if letter != '[' and letter != ']' and letter != ' ' and letter != '\n':
                stack[index].append(letter)
                prev_flag = False
            if letter == ' ':
                if prev_flag == True:
                    skip = 2
                    prev_flag = False
                    continue
                index += 1
                prev_flag = True
        else:
            if letter == ' ' or letter == '\n':
                space_counter += 1
            if space_counter % 2 == 0:
                tmp += letter
            elif space_counter > 0 and tmp != '':
                info_tab.append(int(tmp))
                tmp = ''

    if flag:
        for i in range(info_tab[0]):
            elem = stack[info_tab[1] - 1].pop(0)
            stack[info_tab[2] - 1].insert(0, elem)

for i in range(9):
    if len(stack[i]) > 0:
        ret += stack[i][0]

print(ret)
f.close()
