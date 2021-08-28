# Операторы вхождения: in, not in
# Оператор in возвращает true, если в строке есть необходимая подстрока, иначе возвращает false
# Оператор not in возвращает true, если в строке нет необходимой подстроки, иначе возвращает false
# Операторы сравнения возвращают тип переменных boolean
print('Операторы вхождения')

txt = 'The best things in life are free!'

print('Оператор in: ' + str('free' in txt))
print('Оператор not in: ' + str('expensive' not in txt))