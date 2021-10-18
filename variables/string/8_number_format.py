"""Форматирование чисел."""

print('Форматирование чисел')

int_number = 123232
float_number = 3.14
exp_number = 5e+5
complex_number = 20 - 3j
big_number = 10000000

print('d - десятичный формат: ' + f'{int_number:d}')
print('c - cоответствующий символ Unicode: ' + f'{int_number:c}')
print('b - двоичный формат: ' + f'{int_number:b}')
print('o - восьмеричный формат: ' + f'{int_number:o}')
print('x - шестнадцатеричный формат (в нижнем регистре): ' + f'{int_number:x}')
print('X - шестнадцатеричный формат (в верхнем регистре): ' + f'{int_number:X}')
print('e - экспоненциальная запись (e в нижнем регистре): ' + f'{int_number:e}')
print('E - экспоненциальная запись (E в нижнем регистре): ' + f'{int_number:E}')
print('f - отображать фиксированное количество знаков (по умолчанию = 6): ' + f'{float_number:f}')
print('.2f - отображать два знака после запятой: ' + f'{float_number:.2f}')
print('% - проценты. Умножает на 100 и добавляет % в конце: ' + f'{float_number:%}')
print('Добавить разделитель ",": ' + f'{big_number:,}')
print(f'Вещественная часть: {complex_number.real}, Мнимая часть: {complex_number.imag}')
