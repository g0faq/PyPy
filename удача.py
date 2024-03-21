import random as r

x = r.randint(0, 1000)
lis = [19, 209, 29, 999]
while x not in lis:
    x = r.randint(0, 1000)
if x == lis[0]:
    print('да, сейчас')
if x == lis[1]:
    print('нет')
if x == lis[0]:
    print('да, при встрече')
if x == lis[0]:
    print('нет')