# парсинг файлов
import os
import shutil

KEY_FOR_SEARCH = input('Что ищем? \n')
PASTH_FOR_COPY = input('Куда копировать файлы? \n')


def search():
    for address, dirs, files in os.walk(input('Введите путь старта: \n')):
        if address == PASTH_FOR_COPY:
            continue
        for file in files:
            if file.endswith('.txt') and '$' not in file:
                yield os.path.join(address, file)


def read_from_path_txt(path):
    with open(path) as r:
        for i in r:
            if KEY_FOR_SEARCH in i:
                return copy(path)


def copy(path):
    file_name = path.split('/')[-1] or path.split('\\')[-1]
    count = 1

    while True:
        if os.path.isfile(os.path.join(PASTH_FOR_COPY, file_name)):

            if f'({count - 1})' in file_name:
                file_name = file_name.replace(f'({count - 1})', '')

            file_name = f'({count}).'.join(file_name.split('.'))
            count += 1
        else:
            break

    shutil.copyfile(path, os.path.join(PASTH_FOR_COPY, file_name))
    print('Файл(-ы) скопирован(-ы)', file_name)


for i in search():
    try:
        read_from_path_txt(i)
    except Exception as e:
        with open(os.path.join(PASTH_FOR_COPY, 'errors.txt'), 'w') as r:
            r.write(str(e) + '\n' + i + '\n')
