import datetime as dt
from math import pi, sin

dtb = [int(x) for x in input().split('.')]
dtt = [int(x) for x in input().split('.')]
dt1 = dt.date(dtb[2], dtb[1], dtb[0])
dt2 = dt.date(dtt[2], dtt[1], dtt[0])
T = (dt1 - dt2).days
B = sin((2 * pi * T) / 23) * 100 * -1
B2 = sin((2 * pi * T) / 28) * 100 * -1
B3 = sin((2 * pi * T) / 33) * 100 * -1
print(int(B * 100) / 100)
print(int(B2 * 100) / 100)
print(int(B3 * 100) / 100)