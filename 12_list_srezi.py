t = list(range(1, 21))
e = []
b = t
g = t.copy()
u = t[1::2]  # срез списка. синтаксис: t[start:stop:step], где:
# start - начальное число (включительно). По умолчанию start = 0
# stop - конечное число (не включительно)
# step - шаг. По умолчанию step = 1
p = t[5:]
y = t[:4]
o = t[::3]

print(t)
print(g)
print(p)
print(y)
print(o)
print(u, '\n')

for i in t:
    if i % 2 == 0:  # % - возврящяет остаток от деления
        e.append(i)
        t.remove(i)
else:
    print(e)
    print(t)

print(b, b == t)  # b и t ссылаются на один и тотже список
