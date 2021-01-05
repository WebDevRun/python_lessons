#  рекурсия
# Максимальная глубина рекурсии по умолчанию = 1000

# фукция, возвращающая факториал числа
def some(num):
    if num <= 1:
        return 1
    else:
        return num * some(num-1)


# функция, возвращающая степень числа
def some2(num, st):
    if st == 0:
        return 1
    else:
        return num * some2(num, st-1)


print(some(int(input('Введите число: '))))
print(some2(5, 3))
