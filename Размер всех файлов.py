import os

sp = ['Б', 'КБ', 'МБ', 'ГБ']
v = []

def human_read_format(size):
    a = 0
    while size // 1024 >= 1:
        a += 1
        size /= 1024
    return str(round(size)) + sp[a]


def get_files_sizes():
    for currentdir, dirs, files in os.walk('.'):
        for file in files:
            if os.path.isfile((file)):
                v.append(f'{file} {str(human_read_format(os.path.getsize(file)))}')
    return '\n'.join(v)