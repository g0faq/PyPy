def reverse():
    with open('input.dat', mode='rb') as f:
        data = f.read()
    with open('output.dat', mode='wb') as f:
        f.write(data[::-1])