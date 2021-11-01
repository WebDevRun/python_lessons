"""Работа со списками."""

print('1) Обращение к элементам списка')

frutes_list = ['яблоко', 'банан', 'апельсин', 'ананас']
print(f'исходный список: {frutes_list}')

first_frute = frutes_list[0]
last_frute = frutes_list[-1]
sublist = frutes_list[1:3]
sublist2 = frutes_list[0::2]

print(f'Первый элемент списка: {first_frute}')
print(f'Последний элемент списка: {last_frute}')
print(f'Получение среза списка [1:3]: {sublist}')
print(f'Получение среза списка [0::2]: {sublist2}')

print('2) Добавление элементов в конец списка')

frutes_list += ['абрикос']
print(f'Добавление элемента в конец списка: {frutes_list}')

print('3) Изменение элементов списка')

frutes_list[1] = 'кокос'
frutes_list[2:] = ['арбуз', 'груша']
frutes_list[:1] = ['лимон', 'виноград']
frutes_list[1:-1] = ['папая']

print(f'Изменен элемент списка [1]: {frutes_list}')
print(f'Изменен элемент списка [2:]: {frutes_list}')
print(f'Изменен элемент списка [:1]: {frutes_list}')
print(f'Изменен элемент списка [1:-1]: {frutes_list}')

print('4) удаление элементов списка')

del frutes_list[0]
print(f'Удаленный элемент списка [0]: {frutes_list}')