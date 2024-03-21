pull_ups = 85
push_ups = 190
dumbbells = 180
sit_ups = 185
press = 90
for i in range(28):
    pull_ups += 15
    push_ups += 10
    dumbbells += 20
    sit_ups += 15
    press += 10
    print(f'день: {i + 1}:')
    print(f'подтягивания: {pull_ups}')
    print(f'отжимания: {push_ups}')
    print(f'гантели: {dumbbells}')
    print(f'приседания: {sit_ups}')
    print(f'пресс: {press}')
    print('-' * 15)