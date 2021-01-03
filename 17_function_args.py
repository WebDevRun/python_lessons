# args

def name(h, *args, key):  # *args предобразует параметры в кортеж
    print(h)
    print(key)
    print(args)


def exclusive_items(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            # если в элемента нет в новом списке
            if y not in new_list:
                new_list.append(y)
    if key:
        new_list.sort()
    return new_list


z = [9, 8, 7]
x = [8, 8, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

name(7, 8, 4, 12, 6, key=14)

t = exclusive_items(z, x, c, key=True)

print(t)
