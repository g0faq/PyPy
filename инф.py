snkab = [int(x) for x in input().split()]
s, n, k, a, b = snkab[0], snkab[1], snkab[2], snkab[3], snkab[4]
s = s - n * a
d = 0
count_ir = 0
count_sh = n
if s >= k * b:
    s -= k * b
    count_ir = k
else:
    d = s
    s -= ((s // b) * b)
    count_ir = d // b
count_sh += s // a
print(count_sh, count_ir)