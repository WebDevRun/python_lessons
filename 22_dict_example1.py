price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
new_price = {}
new = {}

for i in price:
    # округление до 2-х знаков после запятой
    new_price[i] = round(price[i] * 0.85, 2)
    print(i)

print('\n')

for key, value in price.items():
    new[value] = key  # reverse ключей на значения
    print(key, value)

print('\n')

for value in price.values():
    print(value)

print('\n')

for key in price.keys():
    print(key)

print('\n')
print(price)
print(new_price)
print(new)
