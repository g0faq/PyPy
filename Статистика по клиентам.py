sl = {}
sp = []
sp2 = []


def get_transactions(t):
    global sl, sp, sp2
    if t != 'print_it':
        x = t.split('-')[1].split(':')[0]
        s = int(t.split(':')[1])
        if x not in sl:
            sl[x] = s
        else:
            sl[x] += s
        sp.append(x)
    else:
        sp2 = sl.keys()
        for elem in sp2:
            print(f'{sp.count(elem)} {elem} {sl[elem]}')
