# Генераторы списков, словарей, множеств
import os

h = [9, 8, 7, 6, 5, 6, 3, 2, 1, 5, 5]
price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
newh = []

for i in h:
    newh.append(i*2)

print(newh, '\n')

# генератор списка.
# Генерация таким способом быстрее в плане быстродействия программы
newh2 = [i*2 for i in h]
# генерация множества
z = {i*2 for i in h}
# генерация словаря
f = {i: i*2 for i in h}

# генератор списка с условием
g = [x for x in h if x % 2 == 0 and x > 2]

t = [os.path.join(z, i)
     for z, x, c in os.walk('./')
     for i in c
     if '.txt' in i or '.py' in i]

new_price = {i: round(price[i] * 0.85, 2) for i in price.keys()}

print(newh2)
print(z)
print(f)
print(g)
print(t, len(t))
print(new_price)
