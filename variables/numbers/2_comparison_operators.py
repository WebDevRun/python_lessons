# Операторы сравления: <, <=, ==, >, >=, !=
# Операторы сравнения возвращают тип переменных boolean
print('Операторы сравления')

num_integer = 1
num_float = 2.13
num_power = 3 ** 2
num_summation = 4 + 4
num_multiply = 5 * 2
num_division = 9 / 3
num_division2 = 10 / 3

print('Сравнение: ' + str(num_integer) + ' < ' + str(num_float) + ' Результат: ' + str(num_integer < num_float)
    + ' Тип переменной: ' + str(type(num_integer < num_float))
)
print('Сравнение: ' + str(num_power) + ' <= 9 Результат: ' + str(num_integer <= 9)
    + ' Тип переменной: ' + str(type(num_integer <= 9))
)
print('Сравнение: ' + str(num_multiply) + ' => 10 Результат: ' + str(num_multiply >= 10)
    + ' Тип переменной: ' + str(type(num_multiply >= 10))
)
print('Сравнение: ' + str(num_integer) + ' > ' + str(num_float) + ' Результат: ' + str(num_integer > num_float)
    + ' Тип переменной: ' + str(type(num_integer > num_float))
)
print('Сравнение: ' + str(num_summation) + ' == ' + str(num_division) + ' Результат: ' + str(num_summation == num_division)
    + ' Тип переменной: ' + str(type(num_summation == num_division))
)
print('Сравнение: ' + str(num_division2) + ' != ' + str(num_power) + ' Результат: ' + str(num_division2 != num_power)
    + ' Тип переменной: ' + str(type(num_division2 != num_power))
)
