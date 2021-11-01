"""Работа с кортежем."""

print('Получение элементов кортежа')

letters = ('a', 'b', 'c', 'd', 'f', 'j')

first_letter = letters[0]
last_letter = letters[-1]
subtuple = letters[1:3]
subtuple2 = letters[0::2]

print(f'Первый элемент: {first_letter}')
print(f'Последний элемент: {last_letter}')
print(f'Получение среза кортежа [1:3]: {subtuple}')
print(f'Получение среза кортежа [0::2]: {subtuple2}')
