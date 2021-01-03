# cycle - цикл
# цикл while

x = int(input())
count = 0
y = 1

while count < x:
    count += 1
    y *= count
else:
    print(y)

x = ''

while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue  # прерывает итерацию цикла
    if y == 'l':
        break  # прерывает весь цикл

    x += y
else:
    print(x)
