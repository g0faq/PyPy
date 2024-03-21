sp = list(range(0, 46))
sp[0] = 1

elem = [4, 20, 24]
if 0 not in sp[elem[1] - 15:elem[2] + 16]:
    for i in range(elem[1], elem[2] + 1):
        sp[i] = 0
print(sp)