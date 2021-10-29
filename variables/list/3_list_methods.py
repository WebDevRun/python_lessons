"""Методы списков."""

print('Методы списков')

list_var = [letter for letter in 'list']
print(str(list_var))

# Метод append(x) добавляет элемент в конец списка
list_var.append('of')
print(f'Результат метода append("of"): {list_var}')

# Метод extend(list) расширяет список, добавляя в конец все элементы другого списка
list_var.extend(list('string'))
print(f'Результат метода extend(list("string")): {list_var}')

# Метод insert(i, x) вставляет на i-ый элемент значение x
list_var.insert(4, ' ')
list_var.insert(6, ' ')
print(f'Результат метода insert(4, " "): {list_var}')

# Метод remove(x) удаляет первый элемент списка со значением x.
# Если такого элемента нет, то выдает ошибку
list_var.remove('of')
print(f'Результат метода remove("of"): {list_var}')

# Метод pop([i]) удалает i-ый элемент и возвращает его.
# Если индекс не указан, то удалается последний элемент
pop_element = list_var.pop(-1)
print(f'Результат метода pop(-1): {list_var}.\n' +
      f'Возвращаемый элемент: {pop_element}')

# Метод index(x, start, end) возвращает индекс первого элемента со значением x.
# При этом поиск ведется от start до end
print(f'Результат метода index("i", -2, -1): {list_var.index("i", -2, -1)}')
print(f'Результат метода index("i"): {list_var.index("i")}')

# Метод count(x) возвращяет количество элементов со значением х
print(f'Результат метода count("t"): {list_var.count("t")}')

# Метод sort(reverse, key) сортирует список
list_var.sort()
print(f'Результат метода sort(): {list_var}')

list_var.sort(reverse = True)
print(f'Результат метода sort(reverse = True): {list_var}')

def sort_len(s):
    return len(s)

sort_list = ['a', 'bbbb', 'ccc', 'dd']
print(f'Исходный список: {sort_list}')

sort_list.sort(key = sort_len)
print(f'Результат метода sort(key = sort_len): {sort_list}')

# Метод reverse() разворачивает список
list_var.reverse()
print(f'Результат метода reverse(): {list_var}')

# Метод copy() поверхностно копирует список
copy_list = list_var.copy()
print(f'Результат метода copy(): {copy_list}')

# Метод clear() очищает список
copy_list.clear()
print(f'Результат метода clear(): {copy_list}')
