# замыкания


def name():
    x = 7

    def name2():
        y = int(input('Введите число: '))
        return x*y

    return name2


h = name()

print('некий код программы')

print(h())
