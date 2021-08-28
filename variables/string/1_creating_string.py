# Строки можно заключать в в одинарные кавычки ('...') или двойные кавычки ("...") с одинаковым результатом
print('Присвоение переменой строку')

str_single_quotes = 'Hello'
str_double_quotes = "world"
str_from_num = str(7)
str_from_bool = str(True)
function_str = f'{54}'

print('str_single_quotes = ' + str_single_quotes + ' Тип переменной: ' + str(type(str_single_quotes)))
print('str_double_quotes = ' + str_double_quotes + ' Тип переменной: ' + str(type(str_double_quotes)))
print('str_from_num = ' + str_from_num + ' Тип переменной: ' + str(type(str_from_num)))
print('str_from_bool = ' + str_from_bool + ' Тип переменной: ' + str(type(str_from_bool)))
print('function_str = ' + function_str + ' Тип переменной: ' + str(type(function_str)))


# Строковые литералы могут занимать несколько строк.
# Одним из способов является использование тройных кавычек: ("""...""") или ('''...''').
# Конец строки автоматически включается в строку, но это можно предотвратить, добавив символ (\) в конце строки
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
