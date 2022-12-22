with open('./01/input.txt') as f:
    data = f.readlines()

ret = 0
tmp = 0

for line in data:
    if line != '\n':
        tmp += int(line)
    else:
        ret = max(ret, tmp) 
        tmp = 0   

print(ret)
f.close()
        
