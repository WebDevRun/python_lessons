# вывод текста или переменной в консоль
print('hello world')

# переменные

none = None  # отсутствие данных

print(type(none), none)

# числa
number1 = 1  # integer - целое число
number2 = 2  # integer - целое число

print(type(number1), number1, type(number2), number2)

number3 = 3.14  # float - дробное число = число с плавающей точкой (заяпятой)
number4 = 21.56  # float - дробное число = число с плавающей точкой (заяпятой)

print(type(number3), number3, type(number4), number4)

comp = 1 + 1j  # complex - комплексное число

print(type(comp), comp)

string1 = 'hello'  # string - строка
string2 = "world"  # string - строка

print(type(string1), string1, type(string2), string2)

li = [1, 1, 'a']  # list - список

print(type(list), list)

tup = (1, 1, 'a')  # tuple - кортеж

print(type(tup), tup)

s = {1, 2, 'a'}  # set - множество

print(type(s), s)

d = {'a': 1, 'b': 2}  # dict - словарь

print(type(d), d)

boo = True  # boolean - логический тип

print(type(boo), boo)

# присвоение переменных

number1, number2 = number2, number1

print(number1, number2)

number1, number2 = number2, number1 + number2

print(number1, number2)

# короткие записи

number3 += number4  # аналогично number3 = number3 + number4
number4 -= number3  # аналогично number3 = number4 = number4 - number3
number2 *= number3  # аналогично number3 = number2 * number3
number1 /= number4  # аналогично number1 = number1 / number4
# number1 //= number2
# number4 %= number3
# number3 **= number1

print(number1, number2, number3, number4)

# списки - list
z, x, *c = [1, 2, 3, 4, 5, 6]
a, *b, w = [3, 7, 85, 23, 234.3]
*r, y, m = [23.5, 54, 456, 45.6]

print(z, x, c)
print(a, b, w)
print(r, y, m)
