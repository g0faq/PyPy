import collections


MESUREMENTS = {'B': 1, 'KB': 2 ** 10, 'MB': 2 ** 20, 'GB': 2 ** 30}


def get_volume(volume, mes):
    return volume * MESUREMENTS[mes.upper()]


def convert_volume():
    with open('input.txt') as in_file:
        data = collections.defaultdict(list)
        for line in map(str.strip, in_file.readlines()):
            fname, volume, mes = line.split()
            name, extansion = fname.split('.')
            data[extansion].append((name, get_volume(volume, mes)))

    with open('output.txt', mode='w', encoding='utf8') as out_file:
        for item in sorted(data.items()):
            total_volume = 0
            for files in item[1]:
                out_file.write(f'{files[0]}.{item[0]}')
                total_volume += files[1]
            out_file.write('-' * 10)
            out_file.write(f'Summary: ')