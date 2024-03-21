LETTERS = ['qwertyuiop', 'sdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'чсмитьбю']


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):

    if len(password) <= 8:
        raise LengthError
    if password.lower() == password:
        raise LetterError
    if password.upper() == password:
        raise LetterError
    if not any([num in password for num in '1234567890']):
        raise DigitError
    for i in range(len(password) - 2):
        part = password[i:i + 3].lower()
        if any(part in string for string in LETTERS):
            raise SequenceError
    return 'ok'