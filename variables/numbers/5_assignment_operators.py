# Операторы присваевания: +=, -=, *=, /=, //=, %=, **=
print('Операторы присваевания')

num_integer = 1
num_float = 2.13
num_summation = 4 + 4
num_subtraction = 97 - 42
num_division2 = 10 / 3
float_from_str = float('10.05')
int_from_str = int('10')
num_a = 57
num_b = 14

print('num_integer = ' + str(num_integer))
num_integer += 2
print('Результат num_integer += 2: ' + str(num_integer) + ' Тип переменной: ' + str(type(num_integer)))

print('num_float = ' + str(num_float))
num_float -= 1.05
print('Результат num_float -= 1.05: ' + str(num_float) + ' Тип переменной: ' + str(type(num_float)))

print('num_subtraction = ' + str(num_subtraction))
num_subtraction *= 0.5
print('Результат num_subtraction *= 0.5: ' + str(num_subtraction) + ' Тип переменной: ' + str(type(num_subtraction)))

print('num_summation = ' + str(num_summation))
num_summation /= 2
print('Результат num_summation /= 2: ' + str(num_summation) + ' Тип переменной: ' + str(type(num_summation)))

print('num_division2 = ' + str(num_division2))
num_division2 //= 3
print('Результат num_division2 //= 3: ' + str(num_division2) + ' Тип переменной: ' + str(type(num_division2)))

print('float_from_str = ' + str(float_from_str))
float_from_str %= 5
print('Результат float_from_str %= 5: ' + str(float_from_str) + ' Тип переменной: ' + str(type(float_from_str)))

print('int_from_str = ' + str(int_from_str))
int_from_str **= 4
print('Результат int_from_str **= 4: ' + str(int_from_str) + ' Тип переменной: ' + str(type(int_from_str)))

print('num_a = ' + str(num_a))
num_a &= 76
print('Результат num_a &= 76: ' + str(num_a) + ' Тип переменной: ' + str(type(num_a)))

print('num_b = ' + str(num_b))
num_b &= 7
print('Результат num_b &= 7: ' + str(num_b) + ' Тип переменной: ' + str(type(num_b)))

print('num_b = ' + str(num_b))
num_b ^= 3
print('Результат num_b ^= 3: ' + str(num_b) + ' Тип переменной: ' + str(type(num_b)))

print('num_a = ' + str(num_a))
num_a >>= 2
print('Результат num_a >>= 2: ' + str(num_a) + ' Тип переменной: ' + str(type(num_a)))

print('num_b = ' + str(num_b))
num_b <<= 2
print('Результат num_b <<= 2: ' + str(num_b) + ' Тип переменной: ' + str(type(num_b)))
