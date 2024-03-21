for i in range(750122, 10 ** 9 + 1):
    if '75' in str(i) and '122' in str(i):
        x = str(i)[str(i).index('75'):str(i).index('122') + 3]
        if x[:2] == '75' and x[3:] == '122':
            print(i, i // 8387 if i % 8387 == 0 else None)
