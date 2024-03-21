n = int(input())
sp = list(map(int, input().split()))

i = 0
res = 0

while True:
    if i >= len(sp) - 2:
        res += sp[i]
        break
    if sp[i] >= sp[i + 1]:
        res += sp[i + 1]
        i += 2
    else:
        res += sp[i]
        i += 1

print(res)