s = [int(x) for x in input().split()]
N, M, x, y = s[0], s[1], s[2], s[3]
mx, my = 0, 0
if N - x < x:
    mx = N - x
else:
    mx = x
if M - y < y:
    my = M - y
else:
    my = y
if my > mx:
    print(mx)
else:
    print(my)