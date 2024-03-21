sp, ma, mi = [x for x in input().split()], (0, ''), (10000, '')
for elem in sp:
    if len(elem) > ma[0]:
        ma = (len(elem), elem)
    if len(elem) < mi[0]:
        mi = (len(elem), elem)
print(f'максимальное: {ma}', f'минимальное: {mi}')