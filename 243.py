data = list(map(int, input().split()))
cost_bilet = data[0]
n_cuper = data[1]
kups = sum(data[2:])
spisok = [500, 100, 50, 10, 5, 1, 2]
sdacha = kups - cost_bilet
answer = []
i = 0
while sdacha > 0:
    a = sdacha // spisok[i]
    answer += [spisok[i]] * a
    sdacha %= spisok[i]
    i += 1
print(answer)