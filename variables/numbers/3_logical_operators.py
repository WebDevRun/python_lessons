# Логические операторы: and, or, not
# В нижеперечисленных примерах:
# Оператор and вернет значение последней переменной, если все значения являющейся true, иначе вернет 0
# Оператор or вернет 0, если все значения false, иначе вернет значение первой переменной являющейся true
print('Логические операторы')

num_integer = 1
num_float = 2.13
num_multiply = 5 * 2

print('Логическая операция: ' + str(num_float) + ' and ' + str(num_integer) + ' and ' + str(num_multiply)
    + ' Результат: ' + str(num_float and num_integer and num_multiply)
    + ' Тип переменной: ' + str(type(num_float and num_integer and num_multiply))
)
print('Логическая операция: 0 and ' + str(num_float) + ' and ' + str(num_integer)
    + ' Результат: ' + str(0 and num_float and num_integer)
    + ' Тип переменной: ' + str(type(0 and num_float and num_integer))
)
print('Логическая операция: ' + str(num_float) + ' or ' + str(num_integer) + ' or ' + str(num_multiply)
    + ' Результат: ' + str(num_float or num_integer or num_multiply)
    + ' Тип переменной: ' + str(type(num_float or num_integer or num_multiply))
)
print('Логическая операция: 0 or 0 or 0'
    + ' Результат: ' + str(0 or 0 or 0)
    + ' Тип переменной: ' + str(type(0 or 0 or 0))
)
print('Логическая операция: not ' + str(num_multiply)
    + ' Результат: ' + str(not num_multiply)
    + ' Тип переменной: ' + str(type(not num_multiply))
)
print('Логическая операция: not ' + str(0)
    + ' Результат: ' + str(not 0)
    + ' Тип переменной: ' + str(type(not 0))
)
