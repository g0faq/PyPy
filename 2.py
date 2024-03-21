def wooden_man_skills(text, divisor, *args, **kwargs):
    s = text.split(divisor)
    for i, k in args:
        for k1, v in kwargs.items():
            if k == k1:
                s[i] = v(s[i])
    return divisor.join(s)