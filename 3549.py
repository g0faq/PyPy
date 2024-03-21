a, b = int(input()), int(input())
if a > b:
    for i in range(b, a + 1):
        for elem in str(i):
            if str(i).count(elem) == 3:
                print(i)
                break
else:
    for i in range(a, b + 1):
        for elem in str(i):
            if str(i).count(elem) == 3:
                print(i)
                break