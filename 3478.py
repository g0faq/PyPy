a = int(input())
b = ''
if len(str(a)) == 3:
    b = '0' + str(a)
elif len(str(a)) == 2:
    b = '00' + str(a)
elif len(str(a)) == 1:
    b = '000' + str(a)
else:
    b = str(a)

if b[::-1] == b:
    print(1)
else:
    print(0)