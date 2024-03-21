n = int(input())
small = (n // 2) * 5
big = (n - 1 - n // 2) * 15
all_time = n * 45 + small + big
h = 9 + all_time // 60
m = all_time % 60
print(h, m)