

sp = [['__C__', '_C___', '_C___', '_C___', '__C__'], ['___', '___', '___', '___', '___'], ['__Д__', '__Д__', '__Д__', '_ДДД_', '_Д_Д_'],
      ['_H_H_', '_H_H_', '_HHH_', '_H_H_', '_H_H_'], ['_ЁЁЁ_', '_Ё___', '_ЁЁЁ_', '_Ё___', '_ЁЁЁ_'],
      ['_M_M_', '_MMM_', '_M_M_', '_M_M_', '_M_M_'], ['___', '___', '___', '___', '___'], ['_У_У_', '__У__', '__У__', '_У___', '_У___'], ['_Ч_Ч_', '_Ч_Ч_', '_ЧЧЧ_', '___Ч_', '___Ч_'],
      ['_И_И_', '_И_И_', '_ИИИ_', '_ИИИ_', '_И_И_'], ['_TTT_', '__T__', '__T__', '__T__', '__T__'], ['_EEE_', '_E___', '_EEE_', '_E___', '_EEE_'],
      ['__Л__', '_Л_Л_', '_Л_Л_', '_Л_Л_', '_Л_Л_'], ['_ЯЯЯ_', '_Я_Я_', '_ЯЯЯ_', '__ЯЯ_', '_Я_Я_']]

res = []
dop = ['_', '_', 'C', '_', '_', '_', '_', '_', '_', '_', 'Д', '_', '_', '_', 'H', '_', 'H', '_', '_', 'Ё', 'Ё', 'Ё', '_', '_', 'M', '_', 'M', '_', '_', '_', '_', '_', 'У', '_', 'У', '_', '_', 'Ч', '_', 'Ч', '_', '_', 'И', '_', 'И', '_', '_', 'T', 'T', 'T', '_', '_', 'E', 'E', 'E', '_', '_', '_', 'Л', '_', '_', '_', 'Я', 'Я', 'Я', '_']
print(''.join(dop))
for q in range(0, 5):
    for elem in sp:
        res += elem[q]
    if q != 0:
        print(res)
    res = ''

