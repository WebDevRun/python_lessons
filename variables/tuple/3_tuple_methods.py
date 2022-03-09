"""Методы кортежей."""

print('Методы кортежей')

vagetables = ('помидор', 'огурец', 'перец', 'лук', 'огурец', 'морковь')

# Метод index(x, start, end) возвращает индекс первого элемента со значением x.
# При этом поиск ведется от start до end
print(f'Результат метода index("огурец", -2, -1): {vagetables.index("огурец", -2, -1)}')
print(f'Результат метода index("перец"): {vagetables.index("перец")}')

# Метод count(x) возвращяет количество элементов со значением х
print(f'Результат метода count("огурец"): {vagetables.count("огурец")}')