def print_long_words(text):
    text += '.'
    w = ''
    c = 0
    for letter in text:
        if letter.isalpha():
            w += letter
            if letter.lower() in 'аоэиуыеёюя' or letter.lower() in 'aeiouy':
                c += 1
        else:
            if c >= 4:
                print(w.lower())
            c = 0
            w = ''