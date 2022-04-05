"""Методы словарей."""

print('Методы словарей')

gender = {
    0: 'man',
    1: 'woman'
}

main_dictionary = {
    'admin': [
        {
            'id': 1,
            'name': 'Alex',
            'nickname': 'aleks734',
            'password': '123456',
            'gender': gender[0]
        },
        {
            'id': 2,
            'name': 'Elena',
            'nickname': 'elen777',
            'password': '349323',
            'gender': gender[1]
        }
    ],
    'user': [
        {
            'id': 3,
            'name': 'Timur',
            'nickname': 'tim544',
            'password': '34578234',
            'gender': gender[0]
        },
        {
            'id': 4,
            'name': 'Rick',
            'nickname': 'rick341',
            'password': '23496512',
            'gender': gender[0]
        },
        {
            'id': 5,
            'name': 'Sam',
            'nickname': 'sam111',
            'password': '8966432',
            'gender': gender[0]
        }
    ]
}

print(f'main_dictionary = {main_dictionary}')

# Метод copy() создает копию словаря
copy_dictionary = main_dictionary.copy()

print(f'copy_dictionary = {copy_dictionary}')

# Метод clear() очищает словарь
copy_dictionary.clear()

print(f'copy_dictionary = {copy_dictionary}')

# Метод fromkeys(seq [, value]) создает словарь с ключами из seq
# и значением value (по умолчанию None).
fromkeys_dict = {}.fromkeys(('one', 'two', 'three'), 2)

print(f'fromkeys_dict = {fromkeys_dict}')

# Метод items() возвращает пары (ключ, значение)
dict_items = fromkeys_dict.items()

print(f'dict_items = {dict_items}')

# Метод keys() возвращает ключи в словаре
print(f'main_dictionary keys = {main_dictionary.keys()}')

# Метод pop() удаляет ключ и возвращает значение
del_item_by_pop = fromkeys_dict.pop('one')

print(f'fromkeys_dict = {fromkeys_dict}')
print(f'del_item = {del_item_by_pop}')

# Метод popitem() удаляет элемент, который был последним
# вставлен в словарь и возвращает пару (ключ, значение)
del_item_by_popitem = fromkeys_dict.popitem()

print(f'fromkeys_dict = {fromkeys_dict}')
print(f'del_item_by_popitem = {del_item_by_popitem}')

# Метод setdefault(key[, default]) возвращает значение ключа, но если его нет,
# создает ключ со значением default (по умолчанию None).
setdefault_key_1 = fromkeys_dict.setdefault('one', 1)
setdefault_key_2 = fromkeys_dict.setdefault('four')

print(f'setdefault_key_1 = {setdefault_key_1}')
print(f'setdefault_key_2 = {setdefault_key_2}')
print(f'fromkeys_dict = {fromkeys_dict}')

# Метод update([other]) обновляет словарь,
# добавляя пары (ключ, значение) из other.
# Существующие ключи перезаписываются. Возвращает None.
fromkeys_dict.update({'five': 5})
fromkeys_dict.update({'four': 4})

print(f'fromkeys_dict = {fromkeys_dict}')

# Метод values() возвращает значения в словаре
values_from_dict = fromkeys_dict.values()
print(f'values_from_dict = {values_from_dict}')
