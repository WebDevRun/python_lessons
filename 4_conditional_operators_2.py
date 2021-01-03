x = [1, 2]

if x == 0:
    x = 1
    print('x был равен нулю')
elif type(x) is int or type(x) is float:  # is - проверка типов переменных
    print('x допустимое значение')
else:
    print('x - недопустимый тип данных')
    x = 1

print(100/x)

# not - логическое отрицание, or -  логическое или, and - логичесткое и
