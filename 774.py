a = input()
a1 = a[:len(a) // 2]
a2 = a[len(a) // 2:]
ans = ''
for i in range(len(a1)):
    ans += a2[i] + a1[i]
if len(a) % 2 != 0:
    ans += a2[-1]
print(ans)