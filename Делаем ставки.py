bets = []


def do_bet(horse, bet):
    global bets
    if 0 < horse <= 10 and horse not in bets and bet > 0:
        bets.append(horse)
        print(f'Ваша ставка в размере {bet} на лошадь {horse} принята')
    else:
        print('Что-то пошло не так, попробуйте еще раз')