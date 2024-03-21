x1, y1, a1, b1, x2, y2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
c = (a1 * 60 + b1) + (((x2 * 60 + y2) - (x1 * 60 + y1)) * 2) % 1440
print(c // 60 % 24, c % 60)