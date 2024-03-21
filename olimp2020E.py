n = int(input())
sp = [int(input()) for x in range(n)]
p = n - 1
print(sp)
for i in range(n):
    if sp[p] > sp[i-1]:
        sp[p] = sp[p]+sp[i]
    else:
        sp[p]=0

    print(sp[p])
print(sp[p])











































a = sp
s = 0
ans = [0] * n
for i in range(n - 1):
    if a[i] > a[0] and a[i] + s > a[i + 1]:
        ans[i] = 1
    else:
        ans[i] = 0
    s += a[i]
if a[n - 1] > a[0]:
    ans[n - 1] = 1
else:
    ans[n - 1] = 0
i = n - 1
while ans[i] == 1:
    i -= 1
while i >= 0:
    ans[i] = 0
    i -= 1
if n == 1:
    ans = [1]
print(*ans)

'''if ans == res:
    print('yes')
else:
    print('no')'''
