"""Функции строк."""

# Функция ord(str) возвращает числовое значение для заданного символа.
print('Результат ord("a"): ' + str(ord('a')))
print('Результат ord("#"): ' + str(ord('#')))
print('Результат ord("€"): ' + str(ord('€')))
print('Результат ord("∑"): ' + str(ord('∑')))

# Функция chr(n) возвращает символьное значение для данного целого числа.
print('Результат chr(97): ' + chr(97))
print('Результат chr(35): ' + chr(35))
print('Результат chr(8364): ' + chr(8364))
print('Результат chr(8721): ' + chr(8721))

# Функция len(s) возвращает длину строки.
s = 'Простая строка.'

print(f'Длина строки {s} = {len(s)}')