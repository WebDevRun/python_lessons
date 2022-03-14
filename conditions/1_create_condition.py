"""Синтаксис условий.

Синтаксис:
if условие(-я):
    программный код (отступ обязательно)
elif др. условие(-я):
    программный код (отступ обязательно)
else:
    программный код (отступ обязательно)
"""

x = 5
y = 166

# Общий вид
if x == y:
    print(f'{str(x)} = {str(y)}')
elif x > y:
    print(f'{str(x)} > {str(y)}')
else:
    print(f'{str(x)} < {str(y)}')

# Вид if else
if x > y:
    print(f'{str(x)} > {str(y)}')
else:
    print(f'{str(x)} < {str(y)}')

# Вид if
if x < y:
    print(f'{str(x)} < {str(y)}')
