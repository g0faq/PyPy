sp = [x for x in input().split()]
s = [x for x in input().split()]
n, e = int(s[0]), s[1]
sp.insert(n, e)
print(*sp)