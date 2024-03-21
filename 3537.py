n = int(input())
res = ''
s = 0
for i in range(1, n):
    res += f'{i}*{i + 1}+'
    s += i * (i + 1)
res = res[:-1]
print(f'{res}={s}')
