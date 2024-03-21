sp = [x[:-1] for x in list(open('input.txt').readlines())]
sp.sort()
sl = {}
for elem in sp:
    if elem not in sl:
        sl[elem] = 1
    else:
        sl[elem] += 1

with open('output.txt', 'w') as f:
    f.writelines(f"{f'{k} {v}'}\n" for k, v in sl.items())