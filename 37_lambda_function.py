# lambda фукции, аннонимные фукции
list_of = [['Adam', 29], ['Jonny', 3*3/12], ['Jess', 25]]


def s(x):
    return x[1]


r = sorted(list_of, key=s)
t = sorted(list_of, key=lambda x: x[1])

e = list(filter(lambda x: x[1] > 18, list_of))

print(r)
print(t)
print(e)
