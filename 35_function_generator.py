# функция генератор

# def some():
#     list_text = []
#     with open('./examples_for_lesson_35/text.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text

# возвращает по одному элементу из цикла
def some():
    with open('./examples_for_lesson_35/text.txt', encoding='utf-8') as r:
        for i in r:
            yield i


for i in some():
    print(i.split())

p = some()

print('\n')
print(next(p))
print(next(p))
print(next(p))
