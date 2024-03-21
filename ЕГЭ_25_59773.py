m = '3?1*57'
sp = []
for i in range(10):
    n = int(f'3{i}157')
    if n % 1991 == 0:
        sp.append(n)
    for j in range(0, 10000):
        n = int(f'3{i}1{str(j)[1::]}57')
        if n % 1991 == 0 and n not in sp:
            sp.append(n)

for elem in sp:
    print(elem, elem // 1991)