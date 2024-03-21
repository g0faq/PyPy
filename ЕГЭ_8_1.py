sp = ['Л', 'Е', 'Т', 'О']
res = set()
for a1 in ['Л', 'Т']:
    for a2 in sp:
        for a3 in sp:
            for a4 in sp:
                s = a1 + a2 + a3 + a4
                if len(s) == 4:
                    res.add(s)
print(res)
print(len(res))