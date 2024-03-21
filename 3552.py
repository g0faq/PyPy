n = int(input())
res = ''
a = 1
while len(res) != n:
    if res.count(str(a)) == a:
        a += 1
    else:
        res += str(a)
print(*[elem for elem in res])