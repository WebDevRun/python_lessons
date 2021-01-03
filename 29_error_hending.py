# обработка ошибок
import os

while True:
    try:
        enter = float(input('Введите: '))
        print(100/enter)
        break
    except ValueError:  # сработает при такой ошибке
        print('Вы ввели не число!!!')
    except ZeroDivisionError:  # сработает при такой ошибке
        print('Делить на 0 нельзя!!!')
    else:
        print('Пользователь молодец.')
    finally:  # сработает в любом случае
        print('Вывод finally')

print('Все нормально\n')

url_list = ['text.txt', 'text1.txt', 'text25.txt', 'text2.txt']
list_defect = []
list_info = []

for url in url_list:
    try:
        r = open(os.path.join(f'{os.getcwd()}/examples_for_lesson_29/{url}'))
        list_info.append(r.read())
    except Exception:
        list_defect.append(url)
        continue

r.close()

print(list_info)
print(list_defect)
