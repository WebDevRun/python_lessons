# 'r' открыть для чтения (по умолчанию)
# 't' открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи. Содержимое файла удаляется.
# Если файла нет, то создается новый
# 'a' открыть для записи в конец файла.
# Если файла нет, то создается новый
# 'b' открыть в динарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'
import os

list_paths = []

for address, dir, file in os.walk('/home/user/Документы/python3'):
    for i in file:
        full_path = os.path.join(address, i)
        list_paths.append(full_path)

# запись в файл
# r = open('./example_for_lesson_23/text.txt', 'w')
# for i in list_paths:
#     r.write(i + '\n')
# r.close()

# чтение из файла
# r = open('./example_for_lesson_23/text.txt')
# read - прочитать файл целиком
# readline - прочитать файл построчно
# readlines - прочитать файл построчно, в виде списка
# for i in r:
#     if '1' in i:
#         print(i)
# text = r.read()
# print(text)
# r.close()

# чтение из файла в бинарном режиме
r = open('./example_for_lesson_23/text.txt', 'rb',)
y = open('./example_for_lesson_23/copy_text.txt', 'wb')

while True:
    var = r.read(1024*1024)
    print(var.__sizeof__())  # сколько оперативной памяти занимает объект
    if var.__sizeof__() == 33:
        break
    y.write(var)

print('end')

r.close()
y.close()
