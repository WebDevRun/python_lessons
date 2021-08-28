# Экранированные последовательности
print('Экранированные последовательности')
# Список экранированных последовательностей:
# \n - новая строка
print('Результат \\n: First line\nSecond line')
# \t - горизонтальный таб
print('Результат \\t: No tab\ttab')
# \r - возврат каретки
print('Результат \\r: Chercher\rTech')
# \b - возврат
print('Результат \\b: String for backspace!\b.')
# \f - подача формы
print('Результат \\f: herCher\fTech')
# \' - одинарная ковычка
print("Результат \\': Isn\'t, they said")
# \" - двойная кавычка
print('Результат \\": He said: \"Good day!\"')
# \\ - обратный слэш
print('Результат \\: \\Backslash\\')
# \v - вертикальный таб
print('Результат \\v: Vertical tab:\vTab string')
# \N - N это число символа Unicode
print('Результат \\N: \110\151')
# \xNN - NN-это шестнадцатеричное значение; \x используется для обозначения следующего шестнадцатеричного значения
print('Результат \\xNN: \x48\x69')
# другие ...

# Побочные эффекты
print('Побочный эффект: C:\tome\name')

# Если вы не хотите, чтобы символы, перед которыми стоит (\), интерпретировались как экранированные последовательности,
# вы можете использовать необработанные строки, добавив букву (r) перед первой кавычкой
print(r'Решение: C:\tome\name')
