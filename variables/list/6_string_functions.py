"""Функции строк."""

print('Функции строк')

letter_list = ['q', 't', 'u', 'y', 'r']
int_list = [1, 2, 4, 10, 121, 56, 768, 98, 2]

print(f'Наибольший элемент в списке int_list: {max(int_list)}')
print(f'Наименьший элемент в списке int_list: {min(int_list)}')

# При передаче в качестве аргумента текстовых строк, байтовых строк или байтовых массивов,
# а так же списка символов, максимальное/минимальное значение будет выбираться исходя
# из порядка следования символов, в таблице соответствующей кодировки.

print(f'Наибольший элемент в списке letter_list: {max(letter_list)}')
print(f'Наименьший элемент в списке letter_list: {min(letter_list)}')

print(f'Длина списка letter_list: {len(letter_list)}')