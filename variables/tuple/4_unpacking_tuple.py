"""Распаковка кортежа."""

animals = ('кот', 'собака', 'корова', 'свинья', 'коза')

# Распаковка кортежа
print('Распаковка кортежа')
(cat, dog, cow, pig, goat) = animals

print(f'cat = {cat}. Тип переменной {type(cat)}')
print(f'cat = {dog}. Тип переменной {type(dog)}')
print(f'cat = {cow}. Тип переменной {type(cow)}')

# Вы можете добавить * к имени переменной,
# и значения будут присвоены переменной в виде списка
(cat, dog, *another_animals) = animals
print(f'cat = {cat}. Тип переменной {type(cat)}')
print(f'dog = {dog}. Тип переменной {type(dog)}')
print(f'another_animals = {another_animals}. Тип переменной {type(another_animals)}')

(cat, *another_animals, goat) = animals
print(f'cat = {cat}. Тип переменной {type(cat)}')
print(f'another_animals = {another_animals}. Тип переменной {type(another_animals)}')
print(f'goat = {goat}. Тип переменной {type(goat)}')
