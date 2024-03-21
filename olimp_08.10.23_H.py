import random

p = random.randint(1, 54)
print(p)

def P(p):
    if p % 2 == 0:
        if p > 36:
            return 'high' , 'side'
        return 'high', 'main'
    else:
        if p > 36:
            return 'low', 'side'
        return 'low', 'main'

while True:
    if P(p)[1] == 'main':
        if P(p + 18)[1] == 'side':
            if P(p + 9)[1] == 'side':
                if P(p + 4)[1] == 'side':
                    if P(p + 2)[1] == 'side':
                        if P(p + 1)[1] == 'side':
                            print('! 36')
                            break
                        else:
                            print('! 35')
                            break
                    else:
                        if P(p + 3)[1] == 'side':
                            print('! 34')
                            break
                        else:
                            print('! 33')
                            break
                else:
                    if P(p + 7)[1] == 'side' and P(p + 7)[0] == 'high':
                        print('! 31')
                        break
                    elif P(p + 7)[1] == 'side' and P(p + 7)[0] == 'low':
                        if P(p + 5)[1] == 'side':
                            print('! 32')
                            break
                        else:
                            print('! 30')
                            break
                    elif P(p + 7)[1] != 'side' and P(p + 7)[0] == 'high':
                        print('! 29')
                        break
                    else:
                        print('! 28')
                    if P(p + 11)[1] == 'side' and P(p + 11)[0] == 'high':
                        print('! 27')
                        break
                    elif P(p + 11)[1] == 'side' and P(p + 11)[0] == 'low':
                        print('! 26')
                        break
                    elif P(p + 12) == 'side':
                        print('! 25')
                        break
                    else:
                        print('! 24')
            else:
                if P(p + 15)[1] == 'side' and P(p + 15)[0] == 'high':
                    print('! 23')
                    break
                elif P(p + 15)[1] == 'side' and P(p + 15)[0] == 'low':
                    print('! 22')
                    break
                elif P(p + 17)[1] == 'side' and P(p + 17)[0] == 'high':
                    print('! 21')
                    break
                elif P(p + 17)[1] == 'side' and P(p + 17)[0] == 'low':
                    print('! 20')
                    break
                else:
                    print('! 19')
        else:
            if P(p + 27)[1] == 'side':
                if P(p + 23)[1] == 'main' and P(p + 23)[0] == 'low':
                    if P(p + 25)[1] == 'side':
                        print('! 12')
                        break
                    else:
                        print('! 10')
                elif P(p + 23)[1] == 'main' and P(p + 23)[0] == 'high':
                    if P(p + 24)[1] == 'side':
                        print('! 13')
                        break
                    else:
                        print('! 11')
                else:
                    if P(p + 21)[1] == 'side' and P(p + 21)[0] == 'high':
                        print('! 17')
                        break
                    elif P(p + 21)[1] == 'side' and P(p + 21)[0] == 'low':
                        if P(p + 19)[1] == 'side':
                            print('! 18')
                            break
                        else:
                            print('! 16')
                if P(p + 22)[1] == 'side':
                    print('! 15')
                    break
                else:
                    print('! 14')
            else:
                if P(p + 32)[1] == 'main' and P(p + 32)[0] == 'low':
                    if P(p + 34)[1] == 'side':
                        print('! 3')
                        break
                    else:
                        print('! 1')
                elif P(p + 32)[1] == 'main' and P(p + 32)[0] == 'high':
                    if P(p + 33)[1] == 'side':
                        print('! 4')
                        break
                    else:
                        print('! 2')
                else:
                    if P(p + 30)[1] == 'side' and P(p + 30)[0] == 'low':
                        if P(p + 28)[1] == 'side':
                            print('! 9')
                            break
                        else:
                            print('! 7')
                    elif P(p + 30)[1] == 'side' and P(p + 30)[0] == 'high':
                        print('! 8')
                        break
                    else:
                        if P(p + 31)[1] == 'side':
                            print('! 6')
                            break
                        else:
                            print('! 5')
    else:
        if P(p - 9)[1] == 'main':
            if P(p - 5)[1] == 'main':
                if P(p - 3)[1] == 'main' and P(p - 3)[0] == 'high':
                    if P(p - 1) == 'main':
                        print('! 37')
                        break
                    else:
                        print('! 39')
                elif P(p - 3)[1] == 'main' and P(p - 3)[0] == 'low':
                    print('! 38')
                else:
                    if P(p - 4)[1] == 'main':
                        print('! 40')
                        break
                    else:
                        print('! 39')
                        break
            if P(p - 7)[1] == 'main' and P(p - 7)[0] == 'low':
                print('! 42')
                break
            elif P(p - 7)[1] == 'main' and P(p - 7)[0] == 'high':
                print('! 43')
                break
            else:
                if P(p - 8) == 'main':
                    print('! 44')
                    break
                else:
                    print('! 45')
        else:
            if P(p - 12) == ('main', 'high'):
                if P(p - 10)[1] == 'main':
                    print('! 46')
                    break
                else:
                    print('! 48')
                    break
            elif P(p - 12) == ('main', 'low'):
                print('! 47')
                break
            else:
                if P(p - 14) == ('main', 'low'):
                    print('! 49')
                    break
                elif P(p - 14) == ('main', 'high'):
                    print('! 50')
                    break
                elif P(p - 16) == ('main', 'low'):
                    print('! 51')
                    break
                elif P(p - 16) == ('main', 'high'):
                    print('! 52')
                    break
                elif P(p - 17)[1] == 'main':
                    print('! 53')
                    break
                else:
                    print('! 54')