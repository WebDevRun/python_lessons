# Декораторы
# Полезны, когда необходимо модифицировать код фукции,
# не вмешиваясь в работу самой функции, не переписывая код функции

def decor(f):
    def wrapper():
        try:
            value = f()
        except Exception:
            print('Повторите ввод: ')
            value = f()
        return value
    return wrapper


@decor  # make = decor(make)
def make():
    enter = float(input('Введите число: '))
    return enter


@decor
def make2():
    enter = float(input('Введите число опять: '))
    return enter


make()
make2()
# h = make
# h()
