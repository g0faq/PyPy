a, b = int(input()), int(input())
if a > b:
    for i in range(b, a + 1):
        if str(i) == str(i)[::-1]:
            print(i)
if a < b:
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            print(i)
else:
    print(a)