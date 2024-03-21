def password_level(password):
    numbers = '1234567890'
    bigletters = 'QWETYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    smallletters = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(password)):
        if password[i] in numbers:
            c1 += 1
        elif password[i] in bigletters:
            c2 += 1
        elif password[i] in smallletters:
            c3 += 1
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif c1 == len(password) or c2 == len(password) or c3 == len(password):
        return 'Ненадежный пароль'
    elif (c2 > 0 and c3 > 0 and c1 == 0) or\
            (c1 > 0 and c2 > 0 and c3 == 0) or\
            (c1 > 0 and c3 > 0 and c2 == 0):
        return 'Слабый пароль'
    elif c1 > 0 and c2 > 0 and c3 > 0:
        return 'Надежный пароль'
