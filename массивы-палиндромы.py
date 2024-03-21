s = [int(x) for x in input().split()]
n, m = s[0], s[1]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if len(a) > len(b):
    for i in range(len(b)):
        if