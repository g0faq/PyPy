n = int(input())
sp = [0, 1]
for i in range(1, n + 1):
    if i == 1:
        continue
    else:
        sp.append(sp[i - 1] * i)
print(sum(sp))