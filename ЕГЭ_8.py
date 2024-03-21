all = 'МАТВЕЙ'
count = 0
for i1 in 'МАТВЕ':
    for i2 in all:
        for i3 in all:
            for i4 in all:
                for i5 in all:
                    for i6 in all:
                        s = i1 + i2 + i3 + i4 + i5 + i6
                        if len(s) == len(set(s)) and 'АЕ' not in s:
                            count += 1

print(count)