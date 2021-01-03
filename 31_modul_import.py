# импорт модулей из фругих файлов.
# После ключевокого слова as будет алиасом
import sys as ss
# импорт конкретных методов или переменных
from examples_for_lesson_31.newmod import newf, k

x = 7

print(newf(x))
print(k)

print(ss.path)  # список адресов, по которым python будет искать модули

# print(dir())
# print(dir(newmod))
# print(help(newmod.newf))
