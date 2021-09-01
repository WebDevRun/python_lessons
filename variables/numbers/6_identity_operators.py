"""Операторы тождественности.

Операторы тождественности: is, is not
Оператор is возвращает true, если обе переменные ссылаются на один объект,
иначе возвращает false
Оператор is not возвращает true, если обе переменные ссылаются на разные
объекты, иначе возвращает false
Операторы сравнения возвращают тип переменных boolean
"""

print('Операторы тождественности')

num_a = 57
num_f = 6
num_g = 6

print('num_f = ' + str(num_f) + ', ' + 'num_g = ' + str(num_g))

print('num_f is num_g = ' + str(num_f is num_g) +
      ' Тип переменной: ' + str(type(num_f is num_g)))

num_d = num_c = 3

print('num_c = ' + str(num_c) + ', ' + 'num_d = ' + str(num_d))

print('num_c is num_d = ' + str(num_c is num_d) +
      ' Тип переменной: ' + str(type(num_c is num_d)))

print('num_a is not num_c = ' + str(num_a is not num_c) +
      ' Тип переменной: ' + str(type(num_a is num_c)))

num_c = 4

print('num_c = ' + str(num_c))

print('num_c is num_d = ' + str(num_c is num_d) +
      ' Тип переменной: ' + str(type(num_c is num_d)))
