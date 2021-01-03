import os  # импортируем модуль os для работы с файловой системой
# walk - возвращает кортеж из папок и файлов,
# находящихся в указанной директории.
# первый элемент - это строка, которую передали в качестве значения
# второй элемент - список папок, находящихся по данному адресу
# третий элемент - список из имен файлов, находящихся по данному адресу

import time

list_txt = []
list_one_day_old = []

for address, dirs, files in os.walk('/home/user/Документы/python3'):
    for file in files:
        # метод path.join возвращает полный путь в файлу
        full = os.path.join(address, file)

        if '.txt' in full:  # если файлы имеют расширение .txt
            list_txt.append(full)

        # если файлы были созданы в течении суток
        if time.time() - os.path.getctime(full) < 86400:
            list_one_day_old.append(full)

print(list_txt, '\n')
print(list_one_day_old)
