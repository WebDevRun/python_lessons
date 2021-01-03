# параметры функции

def count_list(par, par2=False, count=0):  # par - параметр фукции,
    # count = 0 - параметр по умолчанию
    if par2:
        t = type(par[0])
        for i in par:
            count += 1
        return count, t  # вернет кортеж
    else:
        for i in par:
            count += 1
        return count  # вернет целое число


j = [9, 8, 7, 6]
h = ['a', 'a', 'h']
k = [9, 8, 7, 6, 5, 7, 5]

print(count_list(j))
print(count_list(h))
print(count_list(k))
print(count_list('stroka'))
e, r = count_list(k, True, -1)
print(e, r)
print(count_list(k, count=-2))
