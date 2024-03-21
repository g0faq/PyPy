import sys

a = list(map(str.strip, sys.stdin))
sl = {}
for elem in a:
    q = elem.split(' - ')
    x = q[0]
    y = q[1]
    if x in sl:
        sl[x].append(y)
    else:
        sl[x] = [y]
for elem in sl:
    sl[elem] = list(set(sl[elem]))
for elem in sl:
    n = ''
    for i in sl[elem]:
        if n == '':
            n = n + i
        else:
            n = n + '; ' + i
    print(elem, ': ', n, sep='')