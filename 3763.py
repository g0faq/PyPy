spx, spr, spw, res = [], [], [], []

for i in range(int(input())):
    s = input().split()
    s1 = s[1:]
    if 'X' in s1:
        spx.append(s[0])
    if 'W' in s1:
        spw.append(s[0])
    if 'R' in s1:
        spr.append(s[0])

sl = {'e': spx, 'r': spr, 'w': spw}

for i in range(int(input())):
    s = input()
    sp = s.split()
    if s[0] == 'e' or s[0] == 'w' or s[0] == 'r':
        if sp[1] in sl[s[0]]:
            res.append('OK')
        else:
            res.append('Access denied')
    else:
        res.append('Access denied')

print(*res, sep='\n')