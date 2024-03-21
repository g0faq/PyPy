import os
from zipfile import ZipFile

sp = ['Б', 'КБ', 'МБ', 'ГБ']


def human_read_format(size):
    a = 0
    while size // 1024 >= 1:
        a += 1
        size /= 1024
    return str(round(size)) + sp[a]


with ZipFile('input.zip') as myzip:
    print(myzip.namelist())
    print(myzip.filelist)
    for elem in myzip.namelist():
        count = elem.count('/')
        if elem[-1] == '/':
            name = elem[:-1]
            print(f'{" " * ((count - 1) * 2)}{name.split("/")[-1]}')
        else:
            name = elem
            size = human_read_format(os.path.getsize(name))
            print(f'{" " * (count * 2)}{name.split("/")[-1]} {size}') 