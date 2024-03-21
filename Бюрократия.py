name_family = ''
data = ''


def setup_profile(name, vacation_dates):
    global name_family
    global data
    name_family = name
    data = vacation_dates


def print_application_for_leave():
    print(f'Заявление на отпуск в период {data}. {name_family}')


def print_holiday_money_claim(amount):
    print(f'Прошу выплатить {amount} отпускных денег. {name_family}')


def print_attorney_letter(to_whom):
    print(f'На время отпуска в период {data} моим заместителем назначается {to_whom}. {name_family}')
