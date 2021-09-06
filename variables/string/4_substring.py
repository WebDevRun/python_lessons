"""Доступ по индексу."""

print('1) Доступ по индексу')
print('''Индексация строк:
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
''')

word = 'Python'

print('Получение буквы с индексом 0: ' + word[0])
print('Получение буквы с индексом 5: ' + word[5])
print('Получение буквы с индексом -1: ' + word[-1])
print('Получение буквы с индексом -6: ' + word[-6])
print()

# Срезы
print('2) Срезы')
# Получение подстроки word[x:y:z], где:
# x - позиция начала среза (опционально; по умолчанию = 0),
# y - позиция конца среза (опционально; по умолчанию = длине строки; y не входит в срез)
# z - шаг (опционально)
print('Получение подстроки с 0 до 2: ' + word[0:2])
print('Получение подстроки с 2 до 5: ' + word[2:5])
print('Получение подстроки с 2 до конца: ' + word[2:])
print('Получение подстроки с начала до 3: ' + word[:3])
print('Получение каждого втрого символа с начала до конца: ' + word[::2])
print('Получение каждого втрого символа с конца до начала: ' + word[::-2])
print('Получение подстроки с 4 до 43: ' + word[4:43])
print('Получение подстроки с 43 до конца: ' + word[43:])
# Если вы хотите изменить строку, то по сути вы должны создать новую
print('Новая строка: J' + word[1:])
print('Новая строка: ' + word[:2] + 'py')
print('Получение копии строки: ' + word[:])
