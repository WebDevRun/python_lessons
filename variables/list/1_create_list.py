"""Присвоение списков.

Списки - это ссылочный тип данных.
У каждого элемента списка есть свой индекс. Индекс первого элемента = 0
"""

print('1) Присвоение переменной списка')

list_var_function = list('список')
list_var = [1, '2', [3, 4], [5, '6', '7']]

print(f'list_var_function = {list_var_function}. Тип переменной: {str(type(list_var_function))}')
print(f'list_var = {list_var}. Тип переменной: {str(type(list_var))}')

print('2) Генератор списка')

list_from_generator = [letter for letter in 'list']
list_from_generator_2 = [num ** 2 for num in range(10)]

print(f'list_from_generator = {list_from_generator}. Тип переменной: {str(type(list_from_generator))}')
print(f'list_from_generator_2 = {list_from_generator_2}. Тип переменной: {str(type(list_from_generator_2))}')

print('3) Создание копии списка')

list_var_copy = list_var
list_var_copy2 = list_var[:]
list_var_copy3 = list(list_var)

print(f'list_var_copy = {list_var_copy}. Тип переменной: {str(type(list_var_copy))}')
print(f'list_var_copy == list_var: {list_var_copy == list_var}')

print(f'list_var_copy2 = {list_var_copy2}. Тип переменной: {str(type(list_var_copy2))}')
print(f'list_var_copy2 == list_var: {list_var_copy2 == list_var}')

print(f'list_var_copy3 = {list_var_copy3}. Тип переменной: {str(type(list_var_copy3))}')
print(f'list_var_copy3 == list_var: {list_var_copy3 == list_var}')
