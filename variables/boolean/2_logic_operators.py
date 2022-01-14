"""Логические операторы."""

print('1) операторы сравнения')

# == - равенство
# != - неравенсто
# > - больше
# >= - больше либо равно
# < - меньше
# <= - меньше либо равно

print('1 == 1 ->', 1 == 1)
print('A == A ->', 'A' == 'A')
print('hi != Hi ->', 'hi' != 'Hi')
print('2 > 1 ->', 2 > 1)
print('a > A ->', 'a' > 'A')
print('10 >= 10 ->', 10 >= 10)
print('2 >= 1 ->', 2 >= 1)
print('1 < 3 ->', 1 < 3)
print('A < B ->', 'A' < 'B')
print('13 <= 13 ->', 13 <= 13)
print('1 <= 3 ->', 1 <= 3)

print('2) Операторы пренадлежности')

# in - является членом последовательности
# not in - не является членом последовательности

pets = ['dog', 'cat', 'ferret']

print('ferret in pets ->', 'ferret' in pets)
print('re in ferret ->', 're' in 'ferret')
print('fox in pets ->', 'fox' in pets)
print('cow not in pets ->', 'cow' not in pets)

print('3) Операторы тождественности')

# is - является тождественным
# is not - не является тождественным

print('\'3\' is "3" ->', '3' is "3")
print('30 is 300 ->', 30 is 300)
print('2 is not "2" ->', 2 is not "2")

list_a = ['a', 'b', 'c']
list_b = ['a', 'b', 'c']

print(f'{list_a} is {list_b} -> {list_a is list_b}')

list_c = list_a

print(f'{list_c} is {list_a} -> {list_c is list_a}')
