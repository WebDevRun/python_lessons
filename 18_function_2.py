# область видимости

x = 5  # x находится в глобальной области видимости


def name():
    global x  # ссылка на глобальную переменную x
    y = 10  # y находится в локальной области видимости фукции
    x = 11  # функция сначало ишет локальные переменные. Если их нет,
    # то переходит на следующий уровень видимости

    def name2():
        nonlocal y  # изменение значания в материнской фукции
        y += 300
        print(y)

    name2()

    print(x)
    return y


h = name()

print(x)
print(h)
