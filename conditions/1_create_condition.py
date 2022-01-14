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

# общий вид
if x == y:
    print(f'{str(x)} = {str(y)}')
elif x > y:
    print(f'{str(x)} > {str(y)}')
else:
    print(f'{str(x)} < {str(y)}')

# Короткий вид if
if x < y: print(f'{str(x)} < {str(y)}')

# Коротний вид if else
if x > y: print (f'{str(x)} > {str(y)}')
else: print (f'{str(x)} < {str(y)}')
