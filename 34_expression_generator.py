# выражение генератор
import os

h = ['https:\\www.сайт.com', 'https:\\какой-тосайт.net',
     'https:\\другойсайт.com', 'https:\\сайтишка.net',
     'https:\\сайтец.com']

# сгенерирует весь список
n = [x.split('\\')[1] for x in h if '.com' in x]  # генератор списка

# генерирует каждый элемент по обращению к ниму
z = (x.split('\\')[1] for x in h if '.com' in x)  # выражение генератор

for i in z:
    print(i)

e = [z for z in os.walk('./')]

print(e.__sizeof__())

q = (y for y in os.walk('./'))

print(q.__sizeof__())

print(next(q), '\n')  # функция next() возвращает следующий элемент из итерации
print(next(q))
print(q.__sizeof__())

print(n, type(n))
print(type(z))
