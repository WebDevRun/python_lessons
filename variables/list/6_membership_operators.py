"""Операторы вхождения.

Операторы вхождения: in, not in
"""

print('Операторы вхождения')

txt = 'The best things in life are free!'.split(' ')

print(f'txt = {txt}')
print('Оператор in: ' + str('free' in txt))
print('Оператор not in: ' + str('the' not in txt))
