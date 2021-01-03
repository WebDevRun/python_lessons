s = 'sTroka tExta'
path = 'C:/Users/PyHS/Desktop/s.py'

# Эти медоты не изменяют саму строку, а возвращают новую измененную строку
print(s[0:6])  # можно взять срез строки
print(s[5])  # можно получить символ по индексу
print('str' in s)  # есть ли подстрока в строке
print(s.upper())  # переводит все буквы в верхний регистр
print(s.lower())  # переводит все буквы в нижний регистр
# первая буква будет в верхнем регистре, остальные в нижнем
print(s.capitalize())

path1 = path.replace('/', '\\')  # замена одной подстраки на другую
r = path1.split('\\')

q = open('./examples_for_lesson_27/text.txt')
r1 = q.read()
list_znakov = ['(', ')', '"', '\n']
for i in list_znakov:
    if i == list_znakov[-1]:
        r1 = r1.replace(i, ' ')
    r1 = r1.replace(i, '')

r2 = r1.split()  # вернет список из слов
new_text = ' '.join(r2)  # вернет новую строку, разделенную пробелами
q.close()

w = open('./examples_for_lesson_27/text2.txt', 'w')
w.write(r1)
w.write('\n')
w.write(str(r2))
w.close()

print(r1)
print(r2)
print(new_text)
print(s)
print(path1)
print(r)
