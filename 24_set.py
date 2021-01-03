#  set - множества.
# Множество может состоять только из неизменяемых типов данных
# Множество - неупорядоченная коллекция уникальных элементов
# Операции над множествами быстрее
import time

t = {'a', 1, 2, 4, 4, 25, (2, 5)}
x = (1, 2, 3, 4, 5, 6, 7)
y = [1, 2, 3, 4, 5, 6, 7]
u = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}
h = {1, 2, 3, 4, 5, 6, 7}

print(x.__sizeof__())
print(y.__sizeof__())
print(u.__sizeof__())
print(h.__sizeof__())


def f(*args):
    list_new = []
    for i in args:
        for y in i:
            if t not in list_new:
                list_new.append(y)
        return list_new


z = list(range(10000))
b = list(range(5000, 15000))
c = list(range(10000, 20000))

start_list = time.time()
f(z, b, c)
stop_list = time.time() - start_list
print(stop_list)

start_set = time.time()
r = set(z)
m = r.union(set(x), set(c))
stop_set = time.time() - start_set
print(stop_set)


# методы
# Добавит элемент во множество, если его там нет
t.add(6)
# удалить элемент, если есть
t.discard(4)
# удалить элемент. Если такого элемента нет, то произойдет ошибка
t.remove(6)
# Возвращает объединенное множество
p = t.union(h)
# Объединяет множества
t.update(h)
# Возвращает пересечение множества, т.е. найти общие элементы
j = t.intersection(h)
# Возвращает разницу между множествами, т.е. те элементы,
# которые есть в одном множестве, но нет в другом
e = t.difference(h)

print(e)
print(j)
print(t)
print(p)
