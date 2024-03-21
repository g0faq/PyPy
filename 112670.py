def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


a, b = int(input()), int(input())
if a == b == 1:
    print(1)
    quit()
elif (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0) or gcd(a, b) == 1:
    print(-1)
    quit()

flag = False
for i in range(1, int(max(a, b) ** (1 / 2)) + 100):
    if pow(b, i, a) == 0:
        flag = True
        break
if flag:
    print(i)
else:
    print(-1)