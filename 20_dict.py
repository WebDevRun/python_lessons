# dict - словарь. Словарь как и список изменяемый тип данных

d1 = {'a': 7}
d2 = dict(a=7)
d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')
d4 = dict([[1, 2], [3, 4], [5, 6]])

price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

users = {
    'Alex7': {'password': 9856214, 'id': 1295},
    'Jimmy99': {'password': 1235477, 'id': 1235},
    'Bob33': {'password': 5345237, 'id': 14565}
}


def buy():
    pay = 0
    while True:
        enter = input('Что покупаем???\n')
        if enter == 'end':
            break
        pay += price[enter]
    return pay


d1['b'] = 4  # добавляет элемент в словарь
d1['a'] = 8  # изменяет значение элемента в словаре
d1['c'] = 'f'
del d1['c']  # удаляет элемент из словаря

print(d1)
print(d2)
print(d3)
print(d4)

print(buy())
