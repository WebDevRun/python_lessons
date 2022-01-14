"""Создание логических значений."""

print('1) Создание переменной')
true_value = True
false_value = False
boolean_from_str = bool('Срока')
boolean_from_number = bool(1 + 1)
boolean_from_float = bool(-9.7)
math_compare_equal = 1 == 1
math_compare_more = 1 > 2

print(f'true_value = {true_value}. Тип переменной:', type(true_value))
print(f'false_value = {false_value}. Тип переменной:', type(false_value))
print(f'boolean_from_str = {boolean_from_str}. Тип переменной:', type(boolean_from_str))
print(f'boolean_from_number = {boolean_from_number}. Тип переменной:', type(boolean_from_number))
print(f'boolean_from_float = {boolean_from_float}. Тип переменной:', type(boolean_from_float))
print(f'math_compare_equal = {math_compare_equal}. Тип переменной:', type(math_compare_equal))
print(f'math_compare_more = {math_compare_more}. Тип переменной:', type(math_compare_more))

# Некоторые значения, которые являются False
print('2) Некоторые значения, которые являются False')

boolean_false = bool(False)
boolean_none = bool(None)
boolean_0 = bool(0)
boolean_empty_string = bool('')
boolean_empty_tuple = bool(())
boolean_empty_list = bool([])
boolean_empty_dictionary = bool({})

print(f'boolean_false = {boolean_false}. Тип переменной:', type(boolean_false))
print(f'booean_none = {boolean_none}. Тип переменной:', type(boolean_none))
print(f'boolean_0 = {boolean_0}. Тип переменной:', type(boolean_0))
print(f'boolean_empty_string = {boolean_empty_string}. Тип переменной:',
      type(boolean_empty_string))
print(f'boolean_empty_tuple = {boolean_empty_tuple}. Тип переменной:',
      type(boolean_empty_tuple))
print(f'boolean_empty_list = {boolean_empty_list}. Тип переменной:',
      type(boolean_empty_list))
print(f'boolean_empty_dictionary = {boolean_empty_dictionary}. Тип переменной:',
      type(boolean_empty_dictionary))
