def squared():
    a = []
    for i in range(11, 101):
        if i % 10 != 0:
            if len(str(i * i)) != 4:
                a.append(i ** 2)
                if i % 10 != 9:
                    a.append('')
            else:
                a.append(i ** 2)
        else:
            print(*a)
            a.clear()
