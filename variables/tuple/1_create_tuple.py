"""Создание кортежей.

Кортеж - неизменяемый тип данных.
"""

tuple_of_str = ('python', 'java', 'puby', 'C++', 'javascript')
tuple_numbers = 1, 2, 3, 4, 5
tuple_from_stirng = tuple('Hello python!')
tuple_from_list = tuple(['a', 'b', 'c', 'd'])

print(f'tuple_numbers: {tuple_of_str}. Тип переменной: {type(tuple_of_str)}')
print(f'tuple_numbers: {tuple_numbers}. Тип переменной: {type(tuple_numbers)}')
print(f'tuple_numbers: {tuple_from_stirng}. Тип переменной: {type(tuple_from_stirng)}')
print(f'tuple_numbers: {tuple_from_list}. Тип переменной: {type(tuple_from_list)}')
