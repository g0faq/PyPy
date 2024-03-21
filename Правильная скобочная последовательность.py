def bracket_check(test_string):
    x = 0
    y = 0
    for i in range(len(test_string)):
            if '(' in test_string[i]:
                x += 1
            if ')' in test_string[i]:
                y += 1
            if x < y:
                break
        if x == y:
            print('YES')
        else:
            print('NO')