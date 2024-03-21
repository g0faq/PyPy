sp = [x[:-1] for x in list(open('input.txt').readlines())]
sp.sort()
sp_num = []
sl = {}
for elem in sp:
    if elem not in sl:
        sl[elem] = 1
    else:
        sl[elem] += 1
sp_x = []
sl_2 = {}
for k, v in sl.items():
    if v not in sl_2:
        sl_2[v] = []
    sl_2[v].append(k)
    sl_2[v].sort()
    if v not in sp_x:
        sp_x.append(v)

sp_x.sort(reverse=True)

with open('output.txt', 'w') as f:
    f.writelines(f"{f'{e} {x}'}\n" for x in sp_x for e in sl_2[x])