# cycle - цикл
# цикл for

m = 'stroka text'
count = 0

for i in m:
    if i == 't':
        continue
        print('В строке есть буква t')
        count += 1
    print(i)
else:
    print('Цикл завершен, буква t', count)

print('Программа работает')
