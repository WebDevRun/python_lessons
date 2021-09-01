"""Присвоение чисел."""

print('1) Присвоение перeменной число')

num_integer = 1
num_float = 2.13
num_complex = 1 + 2j
int_from_str = int('10')
float_from_str = float('10.05')
complex_from_str = complex('7')
int_from_bool = int(False)
float_from_bool = float(True)

print('Переменная num_integer = ' + str(num_integer) +
      ' Тип переменной: ' + str(type(num_integer)))

print('Переменная num_float = ' + str(num_float) +
      ' Тип переменной: ' + str(type(num_float)))

print('Переменная num_complex = ' + str(num_complex) +
      ' Тип переменной: ' + str(type(num_complex)))

print('Переменная int_from_str = ' + str(int_from_str) +
      ' Тип переменной: ' + str(type(int_from_str)))

print('Переменная float_from_str = ' + str(float_from_str) +
      ' Тип переменной: ' + str(type(float_from_str)))

print('Переменная complex_from_str = ' + str(complex_from_str) +
      ' Тип переменной: ' + str(type(complex_from_str)))

print('Переменная int_from_bool = ' + str(int_from_bool) +
      ' Тип переменной: ' + str(type(int_from_bool)))

print('Переменная float_from_bool = ' + str(float_from_bool) +
      ' Тип переменной: ' + str(type(float_from_bool)))

print()

# Присвоение выражений через операторы: +, -, * и /
# / - такое деление всегда возвращает float,
# т.е. число с плавающей точкой (дробное число)
print('2) Присвоение перeменной выражение')

num_summation = 4 + 4
num_summation_complex = 2 + 2j + 3 + 4j
num_subtraction = 97 - 42
num_multiply = 5 * 2
num_division = 9 / 3
num_division2 = 10 / 3
num_division_complex = (2 + 2j) / (3 + 4j)
sum_num = num_multiply + num_float

print('Сложение: 4 + 4 = ' + str(num_summation) +
      ' Тип переменной: ' + str(type(num_summation)))

print('Сложение комплексных чисел: 2 + 2j + 3 + 4j = ' +
      str(num_summation_complex) + ' Тип переменной: ' +
      str(type(num_summation_complex)))

print('Сложение переменных: num_multiply + num_float = ' +
      str(sum_num) + ' Тип переменной: ' + str(type(sum_num)))

print('Вычитание: 97 - 42 = ' + str(num_subtraction) +
      ' Тип переменной: ' + str(type(num_subtraction)))

print('Умножение: 5 * 2 = ' + str(num_multiply) +
      ' Тип переменной: ' + str(type(num_multiply)))

print('Деление: 9 / 3 = ' + str(num_division) +
      ' Тип переменной: ' + str(type(num_division)))

print('Деление: 10 / 3 = ' + str(num_division2) +
      ' Тип переменной: ' + str(type(num_division2)))

print('Деление комплексных чисел: (2 + 2j) / (3 + 4j) = ' +
      str(num_division_complex) + ' Тип переменной: ' +
      str(type(num_division_complex)))

# Оператор // возвращает целую часть выражения
# Оператор % возвращает остаток выражения
print('Результат выражения: 11 / 4 = ' + str(11 / 4) +
      ' Тип переменной: ' + str(type(11 / 4)))

print('Целая часть выражения: 11 // 4 = ' + str(11 // 4) +
      ' Тип переменной: ' + str(type(11 // 4)))

print('Остаток выражения: 11 % 4 = ' + str(11 %
      4) + ' Тип переменной: ' + str(type(11 % 4)))

# Для вычисления степени можно использовать оператор **
num_power = 3 ** 2
num_power2 = 9 ** 3.2

print('Возведение в степень: 3 ** 2 = ' + str(num_power) +
      ' Тип переменной: ' + str(type(num_power)))

print('Возведение в степень: 9 ** 3.2 = ' + str(num_power2) +
      ' Тип переменной: ' + str(type(num_power2)))
