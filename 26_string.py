# особености написания некоторых символов и экранирование
# \\' - экранирование обратного слэша
# ' \' ' - экранирование ковычки
# ' \" ' - экранирование двойной ковычки
# ' \n ' - перенос строки
# ' \t ' - знак табуляции
# ' \a ' - гудок встроенного системного динамика (работает не везде)
# ' \b ' - Backspace удаляет один символ
# ' \r ' - возврат курсора в начало строки
# ' \v ' - вертикальная табуляция
# ' \f ' - разрыв страницы
# ' \0 ' - символ Null
# ' \N{id} - идентификатор id символа базы Юникода

s = 'Let\'s write a string as "s", ya.ru\\new'
url = r'https:\\www.youtube.com\new'  # r - строка только для чтения
d = ('D:\\')

print(s)
print(url)
print(d)
