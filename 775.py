p = int(input())
if p > 7:
    print((p // 2 // 2 + p % 2) * (p // 2 // 2))
else:
    print((p - 2) // 2)