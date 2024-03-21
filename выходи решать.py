# task 4
res = set()
for n in range(6):
    for a1 in range(6):
        for t in range(6):
            for a2 in range(6):
                for sh in range(6):
                    for a3 in range(6):
                        s = f'{n}{a1}{t}{a2}{sh}{a3}'
                        res.add(s)
print(len(res))