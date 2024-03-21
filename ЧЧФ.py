sp = ['Б', 'КБ', 'МБ', 'ГБ']

def human_read_format(size):
    a = 0
    while size // 1024 >= 1:
        a += 1
        size /= 1024
    return str(round(size)) + sp[a]