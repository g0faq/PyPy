def ask_password():
    f = False
    for i in range(3):
        a = input()
        if a == 'password':
            f = True
            break
    if f:
        print('Пароль принят')
    else:
        print('В доступе отказано')