"""присвоение словарей.

Словарь - неупорядоченная структура данных,
которая позволяет хранить пары «ключ — значение».
Cловарь использует строки в качестве ключей,
однако ключом может являться любой неизменяемый тип данных.
Значением же конкретного ключа может быть что угодно.
Словарь - ссылочный тип данных.
"""

print('1) Присвоение переменной словаря')

definition_dictionary = {
  'информатика': ['программирование', 'системы счисления', 'алгебра логики'],
  'математика': ['алгебра', 'геометрия'],
  'русский язык': ['орфография', 'синтаксис', 'орфоэпия'],
  'физика': ['механика', 'кинематика', 'электродинамика', 'молекулярная физика']
}

gender_dictionary = {
  0: 'муж',
  1: 'жен'
}

users = {
  'Alex7': {'password': 9856214, 'id': 1295},
  'Jimmy99': {'password': 1235477, 'id': 1235},
  'Bob33': {'password': 5345237, 'id': 14565}
}

shot_long_dict = dict(short='dict', long='dictionary')
dict_from_array = dict([(1, 2), (3, 4)])
fromkeys_dict = dict.fromkeys(['a', 'b', 'c'], 100)
generate_dict = {number: number ** 2 for number in range(1, 11)}

print(f'definition_dictionary = {definition_dictionary}')
print(f'gender_dictionary = {gender_dictionary}')
print(f'users = {users}')
print(f'shot_long_dict = {shot_long_dict}')
print(f'dict_from_array = {dict_from_array}')
print(f'fromkeys_dict = {fromkeys_dict}')
print(f'generate_dict = {generate_dict}')

print('2) Получение значения из словаря')

value_by_key_1 = dict_from_array[1]
value_by_key_2 = shot_long_dict['short']

print('Получение значения из словаря dict_from_array по ключу: ',
      value_by_key_1)
print('Получение значения из словаря shot_long_dict по ключу: ',
      value_by_key_2)

print('3) Добавление записи в словарь')

fromkeys_dict['d'] = 200
fromkeys_dict['e'] = fromkeys_dict['d'] + 100

print(f'Новый словарь fromkeys_dict = {fromkeys_dict}')

print('4) Изменение записи в словаре')

users['Alex7']['password'] = 9834223

print(f'Новый словарь users = {users}')

print('5) Удаленние записи из словаря')

del fromkeys_dict['a']

print(f'Новый словарь fromkeys_dict = {fromkeys_dict}')
