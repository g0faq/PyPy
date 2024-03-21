from zipfile import ZipFile
from json import loads

count = 0
with ZipFile('input.zip') as archive:
    for z in archive.filelist:
        if '.json' in z.filename:
            with archive.open(z.filename, 'r') as file:
                data = file.read().decode('utf-8')
                json_data = loads(data)
                if json_data['city'] == 'Москва':
                    count += 1

print(count)