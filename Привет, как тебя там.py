def who_are_you_and_hello():
    is_correct = False
    while not is_correct:
        name = input()
        is_correct = name.isalpha() and name.istitle() and ' ' not in name
    print(f'Привет, {name}!')


# who_are_you_and_hello()