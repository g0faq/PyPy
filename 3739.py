s = input()
x = []
f1 = s.find('f')
f2 = s.rfind('f')
if f1 == f2:
    print(f1)
else:
    print(f1, f2)