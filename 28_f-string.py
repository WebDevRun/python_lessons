enter = input('Your name: ')
var = 'stroka'

a = 'Hello ' + enter
# %s подставляет значение из переменной в сроку
s = 'Hello %s, I am %s' % (enter, 'python')
# метод подставляет значение из переменной в сроку
s1 = 'Hello {1}, I am {0}'.format(enter, 'python')
# f-строки
s2 = f'Hello {enter}, I can do it f-string {len(var)}'

print(a)
print(s)
print(s1)
print(s2)
