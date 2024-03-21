import sys

sp = sys.argv[1:]
s = 0
if len(sp) > 0:
    for i in range(len(sp)):
        try:
            if i % 2 == 0:
                s += int(sp[i])
            else:
                s += -(int(sp[i]))
        except Exception as error:
            print(error.__class__.__name__)
            sys.exit()
    print(s)
else:
    print('NO PARAMS')

