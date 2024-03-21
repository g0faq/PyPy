s = '1'
sp = []
while True:
    try:
        s = input()
        if s != '':
            sp.append(s.split(','))
        else:
            break
    except EOFError:
        break
sp_f = [1] * len(sp[0])

for i in range(1, len(sp)):
    for j in range(len(sp[i])):
        if sp[i][j] != '':
            sp_f[j] = 0

print(sum(sp_f))
res = []
for i in range(len(sp_f)):
    if sp_f[i] == 1:
        res.append(sp[0][i])

res.sort()
for elem in res:
    print(elem)
