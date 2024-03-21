for a in range(10):
    x = int(input())
    b = int(input())
    for i in range(x):
        for j in range(1, b):
           if b % j == 0 and j != 1:
               b += j
               break
    print(b)
