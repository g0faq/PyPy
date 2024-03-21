def palindrome():
    with open('input.dat', mode='rb') as f:
        s = f.read()
        a = s[::-1]
        if s == a:
            return True
        return False