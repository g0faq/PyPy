sp_input = [x[:-1] for x in list(open('input.txt').readlines())]

sp = []
for x in sp_input:
    a = x.split()
    for elem in a:
        sp.append(elem.lower())

sp_1 = []
for elem in sp:
    x = [-(sp.count(elem)), elem]
    if x not in sp_1:
        sp_1.append(x)
sp_1.sort()

with open('output.txt', 'w') as f:
    f.writelines(f"{f'{x[1]} {x[0] * -1}'}\n" for x in sp_1)
