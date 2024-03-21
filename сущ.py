import pymorphy2
from sys import stdin


text = stdin.read().lower().replace('-', ' ')
rus_letters = 'ёйцукенгшщзхъфывапролджэячсмитьбю \t\n'
words = ''.join([c for c in text if c in rus_letters]).split()
morphy = pymorphy2.MorphAnalyzer()
freq_dict = {}
for word in words:
    res = morphy.parse(word)[0]
    if 'NOUN' == res.tag.POS and res.score > 0.5:
        if res.normal_form not in freq_dict:
            freq_dict[res.normal_form] = 0
        freq_dict[res.normal_form] += 1
sp = []
for key, value in freq_dict.items():
    sp.append((key, value))
sp = sorted(sp, key=lambda x: (x[1], x[0]))
print(*map(lambda x: x[0], (sp[-1:-11:-1])))