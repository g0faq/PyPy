sp = input().split()
sp[sp.index(max(sp))], sp[sp.index(min(sp))] = sp[sp.index(min(sp))], sp[sp.index(max(sp))]
print(*sp)
