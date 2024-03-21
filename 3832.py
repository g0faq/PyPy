s = [int(x) for x in input().split()]
for i in range(len(s) + 1):
    if s[i] >= 0 and s[i + 1] >= 0:
        print(s[i], s[i + 1])
        break
    elif s[i] < 0 and s[i + 1] < 0:
        print(s[i], s[i + 1])
        break
    