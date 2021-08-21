# Переменные типа number
# Присвоение чисел
print('1) Присвоение перeменной число: ')

num_integer = 1
num_float = 2.13
num_complex = 1 + 2j
int_from_str = int('10')
float_from_str = float('10.05')
int_from_bool = int(False)
float_from_bool = float(True)

print('Переменная num_integer = ' + str(num_integer) + ' Тип переменной: ' + str(type(num_integer)))
print('Переменная int_from_str = ' + str(int_from_str) + ' Тип переменной: ' + str(type(int_from_str)))
print('Переменная num_float = ' + str(num_float) + ' Тип переменной: ' + str(type(num_float)))
print('Переменная float_from_str = ' + str(float_from_str) + ' Тип переменной: ' + str(type(float_from_str)))
print('Переменная num_complex = ' + str(num_complex) + ' Тип переменной: ' + str(type(num_complex)))
print('Переменная int_from_bool = ' + str(int_from_bool) + ' Тип переменной: ' + str(type(int_from_bool)))
print('Переменная float_from_bool = ' + str(float_from_bool) + ' Тип переменной: ' + str(type(float_from_bool)))
print()

# Присвоение выражений через операторы: +, -, * и /
# / - такое деление всегда возвращает float, т.е. число с плавающей точкой (дробное число)
print('2) Присвоение перeменной выражение: ')

num_summation = 4 + 4
num_summation_complex = 2 + 2j + 3 + 4j
num_subtraction = 97 - 42
num_multiply = 5 * 2
num_division = 9 / 3
num_division2 = 10 / 3
num_division_complex = (2 + 2j) / (3 + 4j)
sum = num_multiply + num_float

print('Сложение: 4 + 4 = ' + str(num_summation) + ' Тип переменной: ' + str(type(num_summation)))
print('Сложение комплексных чисел: 2 + 2j + 3 + 4j = ' + str(num_summation_complex) + ' Тип переменной: ' + str(type(num_summation_complex)))
print('Сложение переменных: num_multiply + num_float = ' + str(sum) + ' Тип переменной: ' + str(type(sum)))
print('Вычитание: 97 - 42 = ' + str(num_subtraction) + ' Тип переменной: ' + str(type(num_subtraction)))
print('Умножение: 5 * 2 = ' + str(num_multiply) + ' Тип переменной: ' + str(type(num_multiply)))
print('Деление: 9 / 3 = ' + str(num_division) + ' Тип переменной: ' + str(type(num_division)))
print('Деление: 10 / 3 = ' + str(num_division2) + ' Тип переменной: ' + str(type(num_division2)))
print('Деление комплексных чисел: (2 + 2j) / (3 + 4j) = ' + str(num_division_complex) + ' Тип переменной: ' + str(type(num_division_complex)))

# Оператор // возвращает целую часть выражения
# Оператор % возвращает остаток выражения
print('Результат выражения: 11 / 4 = ' + str(11 / 4) + ' Тип переменной: ' + str(type(11 / 4)))
print('Целая часть выражения: 11 // 4 = ' + str(11 // 4) + ' Тип переменной: ' + str(type(11 // 4)))
print('Остаток выражения: 11 % 4 = ' + str(11 % 4) + ' Тип переменной: ' + str(type(11 % 4)))

# Для вычисления степени можно использовать оператор **
num_power = 3 ** 2
num_power2 = 9 ** 3.2

print('Возведение в степень: 3 ** 2 = ' + str(num_power) + ' Тип переменной: ' + str(type(num_power)))
print('Возведение в степень: 9 ** 3.2 = ' + str(num_power2) + ' Тип переменной: ' + str(type(num_power2)))
print()

# Операторы сравления: <, <=, ==, >, >=, !=
# Операторы сравнения возвращают тип перенных boolean
print('3) Операторы сравления')
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
print()

# Логические операторы: and, or, not
# В нижеперечисленных примерах:
# Оператор and вернет значение последней переменной, если все значения являющейся true, иначе вернет 0
# Оператор or вернет 0, если все значения false, иначе вернет значение первой переменной являющейся true
print('4) Логические операторы')
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
print()

# Операторы присваевания: +=, -=, *=, /=, //=, %=, **=
print('5) Операторы присваевания')
print('num_integer = '+ str(num_integer))
print('Запись num_integer += 2 эквивалентна num_integer = num_integer + 2')
num_integer += 2
print('num_integer = '+ str(num_integer) + ' Тип переменной: ' + str(type(num_integer)))

print('Запись num_float -= 1.05 эквивалентна num_float = num_float - 1.05')
num_float -= 1.05
print('num_float = '+ str(num_float) + ' Тип переменной: ' + str(type(num_float)))

print('num_subtraction = '+ str(num_subtraction))
print('Запись num_subtraction *= 0.5 эквивалентна num_subtraction = num_subtraction * 0.5')
num_subtraction *= 0.5
print('num_subtraction = '+ str(num_subtraction) + ' Тип переменной: ' + str(type(num_subtraction)))

print('num_summation = '+ str(num_summation))
print('Запись num_summation /= 2 эквивалентна num_summation = num_summation / 2')
num_summation /= 2
print('num_summation = '+ str(num_summation) + ' Тип переменной: ' + str(type(num_summation)))

print('num_division2 = '+ str(num_division2))
print('Запись num_division2 //= 3 эквивалентна num_division2 = num_division2 // 3')
num_division2 //= 3
print('num_division2 = '+ str(num_division2) + ' Тип переменной: ' + str(type(num_division2)))

print('float_from_str = '+ str(float_from_str))
print('Запись float_from_str %= 5 эквивалентна float_from_str = float_from_str % 5')
float_from_str %= 5
print('float_from_str = '+ str(float_from_str) + ' Тип переменной: ' + str(type(float_from_str)))

print('int_from_str = '+ str(int_from_str))
print('Запись int_from_str **= 4 эквивалентна int_from_str = int_from_str ** 4')
int_from_str **= 4
print('int_from_str = '+ str(int_from_str) + ' Тип переменной: ' + str(type(int_from_str)))
print()

# Побитовые операторы: &, |, ^, ~, <<, >>
print('6) Побитовые операторы')
num_a = 57
num_b = 14
print('Бинарный "И" оператор: num_a & num_b = ' + str(num_a & num_b))
print('Бинарный "ИЛИ" оператор: num_a | num_b = ' + str(num_a | num_b))
print('Бинарный "Исключительное ИЛИ" оператор: num_a ^ num_b = ' + str(num_a ^ num_b))
print('Бинарный комплиментарный оператор: num_a ~ num_b = ' + str(~num_a))
print('Побитовый сдвиг влево: num_a << 2 = ' + str(num_a << 2))
print('Побитовый сдвиг вправо: num_b >> 2 = ' + str(num_b >> 2))