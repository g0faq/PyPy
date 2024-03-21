s = input()
x = []
f1 = s.find('f')
f2 = s.rfind('f')
if 'f' not in s:
    print(-2)
elif f1 == f2:
    print(-1)
else:
    print(f2)