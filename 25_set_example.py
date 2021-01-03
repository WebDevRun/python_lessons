new_set = set()

r = open('./examples_for_lesson_25/text.txt')
# множество всех слов без пробелов и знаков переноса строки
r1 = set(r.read().split())
r.close()

r = open('./examples_for_lesson_25/text2.txt')
# множество всех слов без пробелов и знаков переноса строки
r2 = set(r.read().split())
r.close()

new_set.update(r1, r2)
# поиск одинаковых слов из разных множеств
new = r1.intersection(r2)
# поиск слов содержащийся в одном множества и не содержащеихся в другом
new2 = r1.difference(r2)

print(new_set, '\n')
print(new, '\n')
print(new2)
