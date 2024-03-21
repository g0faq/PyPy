h = [int(x) for x in input().split()]
a, b, c = h[0], h[1], h[2]
s = b - a
t = 0
if c <= 0:
    t = s
elif c < s:
    s -= c
    t += s
elif c == s:
    t = 0
elif c > s:
    if s > c - b:
        t += c - b
    else:
        t = s
print(t)
