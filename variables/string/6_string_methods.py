"""Методы строк."""

print('Методы строк')

# Метод capitalize() возвращает копию строки с заглавной первой буквой,
# а остальные в нижнем регистре
print('Результат метода capitalize(): ' + 'python is FUN!'.capitalize())

# Метод lower() возвращает копию строки в нижнем регистре
print('Результат метода lower(): ' + 'Hello World!'.lower())

# Метод upper() возвращает строку, в которой все символы указаны в верхнем регистре.
# Символы и цифры игнорируются.
print('Результат метода upper(): ' + 'Hello my friends!'.upper())

# Метод swapcase() возвращает строку, в которой все прописные буквы являются строчными, и наоборот.
print('Результат метода swapcase(): ' + 'Hello My Name Is PETER'.swapcase())

# Метод encode(encoding=encoding, errors=errors) кодирует строку, используя указанную кодировку, где:
# encoding - cтрока, указывающая используемую кодировку (опциональный; по умолчанию = UTF-8)
# errors - cтрока, указывающая метод ошибки (опциональный). Значениями могут быть:
# 'backslashreplace' - использует обратную косую черту вместо символа, который не удалось закодировать
# 'ignore' - игнорирует символы, который не удалось закодировать
# 'namereplace' - заменяет символ текстом, объясняющим этот символ
# 'strict' - по умолчанию при сбое возникает ошибка
# 'replace' - заменяет символ знаком вопроса
# 'xmlcharrefreplace' - заменяет символ xml символом
txt = "My name is Ståle"

print('Результат метода encode(encoding="ascii", errors="backslashreplace"): ' +
      str(txt.encode(encoding='ascii', errors='backslashreplace')))
print('Результат метода encode(encoding="ascii", errors="ignore"): ' +
      str(txt.encode(encoding='ascii', errors='ignore')))
print('Результат метода encode(encoding="ascii", errors="namereplace"): ' +
      str(txt.encode(encoding='ascii', errors='namereplace')))
print('Результат метода encode(encoding="ascii", errors="replace"): ' +
      str(txt.encode(encoding='ascii', errors='replace')))
print('Результат метода encode(encoding="ascii", errors="xmlcharrefreplace"): ' +
      str(txt.encode(encoding='ascii', errors='xmlcharrefreplace')))

# Метод expandtabs(tabsize) устанавливает размер вкладки на указанное количество пробелов, где:
# tabsize - число, указывающее размер вкладки (опциональный; по умолчанию = 8)
txt = "H\te\tl\tl\to"

print('Результат метода expandtabs(): ' + txt.expandtabs())
print('Результат метода expandtabs(2): ' +  txt.expandtabs(2))

# Метод title() возвращает строку, в которой первый символ в каждом слове прописной.
# Например, заголовок или заголовок.
# Если слово содержит цифру или символ, то первая буква после этого будет преобразована в верхний регистр.
print('Результат метода title(): ' + 'Welcome to my 2nd world'.title())

# Метод replace() заменяет строку другой строкой
print('Результат метода replace(): ' + 'Hello world!'.replace('H', 'J'))

# Метод split() разбивает строку на подстроки и возвращает список,
# если находит экземпляры разделителя, где:
# separator - указывает разделитель, используемый
# при разделении строки (опциональный; по умолчанию = пробел)
# maxsplit - указывает, сколько разделений нужно сделать
# (опциональный; по умолчанию = -1, что означанет "все входжения")
txt = 'apple banana cherry orange'
txt2 = 'apple#banana#cherry#orange'
substr = '#'

print(f'Результат метода split(): ' +
      str(txt.split()))
print(f'Результат метода split("{substr}", 1): ' +
      str(txt2.split(substr, 1)))

# Метод rsplit(separator, maxsplit) разбивает строку на список, начиная справа, где:
# separator - указывает разделитель, используемый
# при разделении строки (опциональный; по умолчанию = пробел)
# maxsplit - указывает, сколько разделений нужно сделать
# (опциональный; по умолчанию = -1, что означанет "все входжения")
print(f'Результат метода rsplit(): ' +
      str(txt.rsplit()))
print(f'Результат метода rsplit("{substr}", 1): ' +
      str(txt2.rsplit(substr, 1)))

# Метод format() принимает переданные аргументы,
# форматирует их и помещает в строку, в которой находятся заполнители {}
age = 36
txt = 'Меня зовут Джон и мне {} лет'

print('Результат метода format(): ' + txt.format(age))

# Так же вы можете резулировать порядок вставки необходимых данных
quantity = 3
itemno = 567
price = 49.95
myorder = "Я хочу заплатить {2} долларов за {0} штуки товара №{1}."

print('Результат метода format() с указанием порядка: ' +
      myorder.format(quantity, itemno, price))

# Метод ljust(length, character) выровняет строку по левому краю, используя
# указанный символ (пробел по умолчанию) в качестве символа заполнения
txt = 'Hello world!'

print('Результат метода ljust(): ' + txt.ljust(20, '_'))

# Метод center(length, character) выровняет строку по центру, используя
# указанный символ (пробел по умолчанию) в качестве символа заполнения
print('Результат метода center(): ' + txt.center(20, '_'))

# Метод rjust(length, character) выровняет строку по правому краю, используя
# указанный символ (пробел по умолчанию) в качестве символа заполнения
print('Результат метода rjust(): ' + txt.rjust(20, '_'))

# Метод lstrip(characters) метод удаляет все начальные символы, где:
# characters - набор символов для удаления в качестве начальных символов
txt = '    Hello, world!        '
txt2 = ',,,,,ssaaww.....banana,ssaaww.'
substr = ',.asw'

print('Результат метода lstrip(): ' + txt.lstrip())
print(f'Результат метода lstrip("{substr}"): ' + txt2.lstrip(substr))

# Метод strip(characters) удаляет любые начальные символы и
# конечные символы, где:
# characters - набор символов для удаления в качестве начальных/конечных символов
print('Результат метода strip(): ' + txt.strip())
print(f'Результат метода strip("{substr}"): ' + txt2.strip(substr))

# Метод rstrip(characters) удаляет любые завершающие символы (символы в конце строки),
# пробел является завершающим символом по умолчанию для удаления.
print('Результат метода rstrip(): ' + txt.rstrip())
print(f'Результат метода rstrip("{substr}"): ' + txt2.rstrip(substr))

# Метод count(value, start, end) возвращает количество раз,
# когда указанное значение появляется в строке, где:
# value - строка для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент, целое число;
# по умолчанию = длина строки)
txt = 'I love apples, apple are my favorite fruit'
substr = 'apple'

print(f'Результат метода count("{substr}"): ' + str(txt.count(substr)))
print(f'Результат метода count("{substr}", 10, 24): ' + str(txt.count(substr, 10, 24)))

# Метод isalnum() возвращает значение True, если все символы буквенно-цифровые,
# то есть буквы алфавита (a-z, A-Z) и цифры (0-9)
print('Результат метода isalnum(): ' +
      str('WelcomeToMyWorld'.isalnum()))
print('Результат метода isalnum(): ' +
      str('Hello, welcome to my world.'.isalnum()))

# Метод isalpha() возвращает значение True, если все символы буквенные,
# то есть буквы алфавита (a-z, A-Z)
print('Результат метода isalpha(): ' + str('Company'.isalpha()))
print('Результат метода isalpha(): ' + str('Company10'.isalpha()))

# Метод isascii() возвращает значение True, если все символы являются символами ascii
print('Результат метода isascii(): ' + str('Company123'.isascii()))
print('Результат метода isascii("😀"): ' + str('😀'.isascii()))

# Метод isdecimal() возвращает значение True,
# если все символы являются десятичными (0-9)
num_str = '\u0030'
num_str2 = '\u00B2'
num_str3 = '1.3'
num_str4 = '-1'
NaN_str = 'Not a number'

print(f'Результат метода isdecimal("{num_str}"): ' + str(num_str.isdecimal()))
print(f'Результат метода isdecimal("{num_str2}"): ' + str(num_str2.isdecimal()))
print(f'Результат метода isdecimal("{num_str3}"): ' + str(num_str3.isdecimal()))
print(f'Результат метода isdecimal("{num_str4}"): ' + str(num_str4.isdecimal()))
print(f'Результат метода isdecimal("{NaN_str}"): ' + str(NaN_str.isdecimal()))

# Метод isdigit() возвращает значение True, если все символы являются цифрами,
# в противном случае значение False
print(f'Результат метода isdigit("{num_str}"): ' + str(num_str.isdigit()))
print(f'Результат метода isdigit("{num_str2}"): ' + str(num_str2.isdigit()))
print(f'Результат метода isdigit("{num_str3}"): ' + str(num_str3.isdigit()))
print(f'Результат метода isdigit("{num_str4}"): ' + str(num_str4.isdigit()))
print(f'Результат метода isdigit("{NaN_str}"): ' + str(NaN_str.isdigit()))

# Метод isnumeric() возвращает значение True, если все символы числовые (0-9),
# в противном случае значение False.
# '-1' и '1.5' не считаются числовыми значениями, поскольку все символы
# в строке должны быть числовыми,
# а подстроки '-' и '.' не являются числами

print(f'Результат метода isnumeric("{num_str}"): ' + str(num_str.isnumeric()))
print(f'Результат метода isnumeric("{num_str2}"): ' + str(num_str2.isnumeric()))
print(f'Результат метода isnumeric("{num_str3}"): ' + str(num_str3.isnumeric()))
print(f'Результат метода isnumeric("{num_str4}"): ' + str(num_str4.isnumeric()))
print(f'Результат метода isnumeric("{NaN_str}"): ' + str(NaN_str.isnumeric()))

# Метод isidentifier() возвращает значение True, если строка является
# допустимым идентификатором, в противном случае значение False.
# Строка считается допустимым идентификатором, если она содержит только
# буквенно-цифровые буквы (a-z, A-Z) и (0-9) или символы подчеркивания (_).
# Допустимый идентификатор не может начинаться с числа или содержать пробелы.
print('Результат метода isidentifier(): ' + str('Company10'.isidentifier()))
print('Результат метода isidentifier(): ' + str('2bring'.isidentifier()))

# Метод islower() возвращает значение True, если все символы в нижнем регистре,
# в противном случае значение False
print('Результат метода islower(): ' + str('2bring'.islower()))

# Метод isupper() возвращает значение True, если все символы указаны
# в верхнем регистре, в противном случае значение False
print('Результат метода isupper(): ' + str('MY NAME IS PETER!'.isupper()))

# Метод join(iterable) принимает итерируемые переменные и
# объединяет их в одну строку
my_tuple = ('John', 'Peter', 'Vicky')

print('Результат метода join(): ' + '; '.join(my_tuple))

# Метод maketrans(x, y, z) возвращает таблицу сопоставления,
# которую можно использовать с методом translate() для замены указанных символов, где:
# x - Если указан только один параметр, это должен быть словарь, описывающий, как выполнить замену.
# Если указаны два или более параметра, этот параметр должен быть строкой,
# указывающей символы, которые вы хотите заменить (обязательный аргумент)
# y - Строка той же длины, что и параметр x. Каждый символ в первом параметре будет заменен
# соответствующим символом в этой строке. (опциональный аргумент)
# z - Строка, описывающая, какие символы следует удалить из исходной строки. (опциональный аргумент)

# Метод translate(table) возвращает строку, в которой некоторые указанные символы заменены символом,
# описанным в словаре или в таблице сопоставления.
txt = 'Good night Sam!'
x = 'mSa'
y = 'eJo'
z = 'odnght'
mytable = txt.maketrans(x, y, z)

print('Результат метода maketrans(): ' + str(mytable))
print('Результат метода translate(): ' + txt.translate(mytable))

# Метод partition(value) выполняет поиск указанной строки и
# разбивает строку на кортеж, содержащий три элемента.
# Первый элемент содержит часть перед указанной строкой.
# Второй элемент содержит указанную строку.
# Третий элемент содержит часть после строки.
txt = 'I could eat bananas all day'
substr = 'bananas'
substr2 = 'apple'

print(f'Результат метода partition("{substr}"): ' +
      str(txt.partition(substr)))
print(f'Результат метода partition("{substr2}"): ' +
      str(txt.partition(substr2)))

# Метод rpartition(value) выполняет поиск последнего вхождения указанной строки и
# разбивает строку на кортеж, содержащий три элемента.
# Первый элемент содержит часть перед указанной строкой.
# Второй элемент содержит указанную строку.
# Третий элемент содержит часть после строки.
txt = 'I could eat bananas all day, bananas are my favorite fruit'

print(f'Результат метода rpartition("{substr}"): ' + str(txt.rpartition(substr)))
print(f'Результат метода rpartition("{substr2}"): ' + str(txt.rpartition(substr2)))

# Метод index(value, start, end) находит первое вхождение
# указанного значения, где:
# value - строка для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент, целое число;
# по умолчанию = длина строки)
# Метод index() вызывает исключение, если значение не найдено.
txt = 'Hello, welcome to my world. It is beautifully world.'
substr = 'world.'

print(f'Результат метода index("{substr}"): ' +
      str(txt.index(substr)))
print(f'Результат метода index("{substr}", 26, 52): ' +
      str(txt.index(substr, 26, 52)))

# Метод rindex(value, start, end) находит последнее вхождение
# указанного значения, где:
# value - Значение для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент; целое число;
# по умолчанию = длина строки)
# Метод rindex() вызывает исключение, если значение не найдено.
print(f'Результат метода rindex("{substr}"): ' +
      str(txt.rindex(substr)))
print(f'Результат метода rindex("{substr}", 0, 29): ' +
      str(txt.rindex(substr, 0, 29)))

# Метод find(value, start, end) находит первое вхождение указанного значения, где:
# value - Значение для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент; целое число;
# по умолчанию = длина строки)
# Метод find() возвращает -1, если значение не найдено.
# Метод find() почти такой же, как метод index(), с той лишь разницей,
# что метод index() вызывает исключение, если значение не найдено.
txt = 'Hello, welcome to my world.'
substr = 'e'

print(f'Результат метода find("{substr}"): ' + str(txt.find(substr)))
print(f'Результат метода find("{substr}", 5, 10): ' + str(txt.find(substr, 5, 10)))

# Метод rfind(value, start, end) находит последнее вхождение указанного значения, где:
# value - Значение для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент; целое число;
# по умолчанию = длина строки)
# Метод rfind() возвращает -1, если значение не найдено.
# Метод rfind() почти такой же, как метод index(), с той лишь разницей,
# что метод index() вызывает исключение, если значение не найдено.
print(f'Результат метода rfind("{substr}"): ' + str(txt.rfind(substr)))
print(f'Результат метода rfind("{substr}", 5, 10): ' + str(txt.rfind(substr, 5, 10)))

# Метод splitlines(keeplinebreaks) разбивает строку на список, где:
# Указывает, следует ли включать разрывы строк (True) или нет (False)
# (опциональный; по умолчанию = False)
# Разделение выполняется при разрывах строк.
print('Результат метода splitlines(): ' +
      str('Thank you for the music\nWelcome to the jungle'.splitlines(True)))

# Метод startswith(value, start, end) возвращает значение True, если строка начинается
# с указанного значения, в противном случае значение False, где:
# value - Значение для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент; целое число;
# по умолчанию = длина строки)
txt = 'Hello, welcome to my world.'
substr = 'Hello'
substr2 = 'my world.'

print(f'Результат метода startswith("{substr}"): ' +
      str(txt.startswith(substr)))
print(f'Результат метода startswith("{substr}", 5, 11): ' + 
      str(txt.startswith(substr, 5, 11)))

# Метод endswith(value, start, end) возвращает значение True, если строка заканчивается
# указанным значением, в противном случае значение False, где:
# value - Значение для поиска (обязательный аргумент)
# start - позиция начала поиска (опциональный аргумент; целое число;
# по умолчанию = 0)
# end - позиция конца поиска (опциональный аргумент; целое число;
# по умолчанию = длина строки)
print(f'Результат метода endswith("{substr2}"): ' +
      str(txt.endswith(substr2)))
print(f'Результат метода endswith("{substr2}", 5, 11): ' +
      str(txt.endswith(substr2, 5, 11)))

# Метод zfill(len) добавляет нули (0) в начало строки,
# пока она не достигнет указанной длины, где:
# len - число, указывающее желаемую длину строки (обязательное)
# Если значение параметра len меньше длины строки, заполнение не выполняется.
len_value = 10

print(f'Результат метода zfill({len_value}): ' + 'hello'.zfill(len_value))
print(f'Результат метода zfill({len_value}): ' + 'welcome to the jungle'.zfill(len_value))
