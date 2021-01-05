# хвостовая рекурсия

title = {
    'Неклеточные': {
        'Вирусы': 100,
        'Фаги': 56
        },
    'Клеточные': {
        'Прокариоты': {
            'Бактерии': 576,
            'Архебактерии': 256
        },
        'Эукариоты': {
            'Растения': 788,
            'Животные': {
                'Одновлеточные': 257,
                'Многоклеточные': 258
            },
            'Грибы': 256,
            'Лишайники': 73
        }
    }
}


def rec(sl, search):
    if search in sl.keys():
        return sl[search]

    for n in sl.values():
        if type(n) == dict:
            ret = rec(n, search)
            if ret:
                return ret


print(rec(title, input('Введите \n')))
